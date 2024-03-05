

#!/usr/bin/env python3

import os
import re

class ScanDir:
    @staticmethod
    def format_exts(exts):
        """Format extensions: make them lowercase and ensure they start with a dot."""
        formatted = set()
        for ext in exts:
            if not ext.startswith('.'):
                ext = f'.{ext}'
            formatted.add(ext.lower())
        return tuple(formatted)

    @staticmethod
    def scandir_recursive(path, mask="", ext_tuple=(), folders=True, files=True,
                          hidden=False, min_name_len=0, max_name_len=9999, depth=0,
                          max_find_items=0):
        """Recursively scan directory with various filtering options."""
        if not os.path.isdir(path):
            raise FileNotFoundError("Directory doesn't exist.")
        
        mask_re = re.compile(mask)
        ext_tuple = ScanDir.format_exts(ext_tuple)

        def inner_scan(dir_path, current_depth):
            if max_find_items > 0 and len(found_items) >= max_find_items:
                return  # Stop if max items limit is reached
            try:
                for entry in os.scandir(dir_path):
                    if not hidden and entry.name.startswith('.'):
                        continue
                    if not min_name_len <= len(entry.name) <= max_name_len:
                        continue
                    if entry.is_dir(follow_symlinks=False):
                        if folders and mask_re.match(entry.name) and (not ext_tuple or entry.name.lower().endswith(ext_tuple)):
                            found_items.append(entry)
                        if depth != 0 and (current_depth < depth or depth == -1):
                            inner_scan(entry.path, current_depth + 1 if depth > 0 else -1)
                    elif files and entry.is_file() and mask_re.match(entry.name) and (not ext_tuple or entry.name.lower().endswith(ext_tuple)):
                        found_items.append(entry)
            except (FileNotFoundError, NotADirectoryError, PermissionError):
                pass

        found_items = []
        inner_scan(path, 0)
        return found_items

    @staticmethod
    def scandir_recursive_sorted(path, mask="", ext_tuple=(), folders=True, files=True,
                                 hidden=False, min_name_len=0, max_name_len=9999, depth=0,
                                 max_find_items=0, files_before_dirs=False, reverse=False):
        """Create a sorted scandir_recursive tree."""
        tree = ScanDir.scandir_recursive(path, mask, ext_tuple, folders, files,
                                         hidden, min_name_len, max_name_len, depth, max_find_items)
        if depth == 0:
            tree.sort(key=lambda entry: (
                not entry.is_dir() if files_before_dirs else entry.is_dir(),
                entry.name.casefold()), reverse=reverse)
        else:
            tree.sort(key=lambda entry: entry.path.casefold(), reverse=reverse)
        return tree
if __name__ == '__main__':
    path_to_scan = '.'  # Current directory
    mask = ''  # No regex mask
    ext_tuple = ('.py',)  # Look for Python files
    folders = True
    files = True
    hidden = False
    depth = -1  # Unlimited depth
    max_find_items = 0  # No limit on items to find
    output_file_path = 'scan_results.txt'  # File to save the scan results

    # Call the scandir_recursive or scandir_recursive_sorted method
    items = ScanDir.scandir_recursive(path_to_scan, mask, ext_tuple, folders, files, hidden, depth=depth, max_find_items=max_find_items)
    
    # Open the file in write mode
    with open(output_file_path, 'w') as output_file:
        for item in items:
            output_file.write(item.path + '\n')  # Write each item's path to the file

    print(f"Scan results saved to {output_file_path}")

