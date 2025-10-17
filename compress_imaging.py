#!/usr/bin/env python3
"""
Imaging Data Compression Tool
Compresses old TIFF/OME-TIFF files to save storage space
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime, timedelta
import subprocess
import hashlib
import shutil

def calculate_checksum(filepath):
    """Calculate SHA256 checksum of a file"""
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            sha256.update(chunk)
    return sha256.hexdigest()

def compress_tiff(input_file, output_file, compression='lzw'):
    """Compress TIFF file using ImageMagick or tifffile"""
    try:
        # Try using tifffile (Python library)
        from tifffile import imread, imwrite
        img = imread(str(input_file))
        imwrite(str(output_file), img, compression=compression)
        return True
    except ImportError:
        # Fallback to ImageMagick command line
        try:
            cmd = ['convert', str(input_file), '-compress', compression.upper(), str(output_file)]
            subprocess.run(cmd, check=True, capture_output=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(f"ERROR: Cannot compress {input_file}. Install tifffile or ImageMagick.")
            return False

def find_old_tiffs(root_dir, days_old=90):
    """Find all TIFF files older than specified days"""
    cutoff_date = datetime.now() - timedelta(days=days_old)
    old_tiffs = []
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.tif', '.tiff')):
                filepath = Path(root) / file
                mtime = datetime.fromtimestamp(filepath.stat().st_mtime)
                if mtime < cutoff_date:
                    old_tiffs.append(filepath)
    
    return old_tiffs

def main():
    parser = argparse.ArgumentParser(description='Compress old imaging data to save storage')
    parser.add_argument('--input', required=True, help='Input directory to search')
    parser.add_argument('--days-old', type=int, default=90, help='Age threshold in days (default: 90)')
    parser.add_argument('--compression', default='lzw', choices=['lzw', 'zlib', 'jpeg'], 
                       help='Compression algorithm')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be compressed without doing it')
    parser.add_argument('--backup-dir', help='Directory to backup originals before compression')
    
    args = parser.parse_args()
    
    print(f"\n{'='*60}")
    print(f"IMAGING DATA COMPRESSION TOOL")
    print(f"{'='*60}")
    print(f"Input directory: {args.input}")
    print(f"Age threshold: {args.days_old} days")
    print(f"Compression: {args.compression}")
    if args.dry_run:
        print("DRY RUN MODE - No files will be modified")
    print(f"{'='*60}\n")
    
    # Find old TIFF files
    print("Searching for old TIFF files...")
    old_tiffs = find_old_tiffs(args.input, args.days_old)
    
    if not old_tiffs:
        print(f"No TIFF files older than {args.days_old} days found.")
        return
    
    # Calculate total size
    total_size = sum(f.stat().st_size for f in old_tiffs)
    total_size_gb = total_size / (1024**3)
    
    print(f"\nFound {len(old_tiffs)} old TIFF files")
    print(f"Total size: {total_size_gb:.2f} GB")
    print(f"Expected savings: {total_size_gb * 0.3:.2f} - {total_size_gb * 0.5:.2f} GB (30-50% reduction)\n")
    
    if args.dry_run:
        print("Files that would be compressed:")
        for f in old_tiffs[:10]:  # Show first 10
            print(f"  - {f}")
        if len(old_tiffs) > 10:
            print(f"  ... and {len(old_tiffs) - 10} more")
        return
    
    # Confirm before proceeding
    response = input(f"Compress {len(old_tiffs)} files? This cannot be undone. (yes/no): ")
    if response.lower() != 'yes':
        print("Aborted.")
        return
    
    # Process files
    compressed_count = 0
    space_saved = 0
    failed = []
    
    for i, input_file in enumerate(old_tiffs, 1):
        print(f"[{i}/{len(old_tiffs)}] Processing {input_file.name}...", end=' ')
        
        # Calculate original checksum
        original_checksum = calculate_checksum(input_file)
        original_size = input_file.stat().st_size
        
        # Create output path (same location, add .compressed suffix temporarily)
        output_file = input_file.with_suffix('.compressed' + input_file.suffix)
        
        # Backup if requested
        if args.backup_dir:
            backup_path = Path(args.backup_dir) / input_file.name
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(input_file, backup_path)
        
        # Compress
        if compress_tiff(input_file, output_file, args.compression):
            compressed_size = output_file.stat().st_size
            reduction = (1 - compressed_size / original_size) * 100
            
            # Replace original with compressed
            input_file.unlink()
            output_file.rename(input_file)
            
            # Update checksum file
            checksum_file = input_file.with_suffix(input_file.suffix + '.sha256')
            new_checksum = calculate_checksum(input_file)
            with open(checksum_file, 'w') as f:
                f.write(f"{new_checksum}  {input_file.name}\n")
            
            compressed_count += 1
            space_saved += (original_size - compressed_size)
            print(f"✓ Saved {reduction:.1f}%")
        else:
            failed.append(input_file)
            print(f"✗ Failed")
    
    # Summary
    print(f"\n{'='*60}")
    print(f"COMPRESSION COMPLETE")
    print(f"{'='*60}")
    print(f"Successfully compressed: {compressed_count}/{len(old_tiffs)} files")
    print(f"Space saved: {space_saved / (1024**3):.2f} GB")
    print(f"Failed: {len(failed)} files")
    if failed:
        print("\nFailed files:")
        for f in failed:
            print(f"  - {f}")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    main()
