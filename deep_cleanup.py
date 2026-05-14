import os
import re

def clean_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Background replacements (Dark to Light)
    replacements = [
        ('#111ffffff', '#ffffff'),
        ('#111fff', '#ffffff'),
        ('background-color: #1a1a1a', 'background-color: #ffffff'),
        ('background-color: #000', 'background-color: #ffffff'),
        ('background: rgba(17, 17, 17, 0.98)', 'background: #ffffff'),
        ('background: rgba(17, 17, 17, 0.95)', 'background: #ffffff'),
    ]

    for old, new in replacements:
        content = content.replace(old, new)

    # 2. FIX: Ensure inputs don't have blue text
    # The user complained about blue input text.
    content = content.replace('color: #0d6efd', 'color: #111111')
    
    # 3. Restore blue for HEADERS, BUTTONS, and BADGES (where it belongs)
    restore_blue = [
        ('h1 { color: #111111', 'h1 { color: #0d6efd'),
        ('h2 { color: #111111', 'h2 { color: #0d6efd'),
        ('h3 { color: #111111', 'h3 { color: #0d6efd'),
        ('h4 { color: #111111', 'h4 { color: #0d6efd'),
        ('h5 { color: #111111', 'h5 { color: #0d6efd'),
        ('background: linear-gradient(135deg, #111111,', 'background: linear-gradient(135deg, #0d6efd,'),
        ('color: #111111 !important; } .header-title', 'color: #0d6efd !important; } .header-title'),
        ('class="badge badge-blue" style="color: #111111', 'class="badge badge-blue" style="color: #0d6efd'),
    ]

    for old, new in restore_blue:
        content = content.replace(old, new)

    # 4. Global CSS normalization for inputs
    if file_path.endswith('.css'):
        # Force input color to be dark
        content = re.sub(r'(input|textarea|select|form-control)\s*\{([^}]*)\}', 
                         lambda m: m.group(0).replace('#0d6efd', '#111111'), 
                         content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

root_dir = r'c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel'
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(('.html', '.css')):
            clean_file(os.path.join(root, file))

print('Fixed input colors and normalized theme.')
