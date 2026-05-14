import os
import re

def normalize_panel(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Background Replacements (Force Light)
    bg_replacements = [
        ('background-color: #000', 'background-color: #ffffff'),
        ('background-color:#000', 'background-color:#ffffff'),
        ('background-color: #111', 'background-color: #ffffff'),
        ('background-color: #111111', 'background-color: #ffffff'),
        ('background-color:#111', 'background-color:#ffffff'),
        ('background: #111', 'background: #0d6efd'), # Likely buttons
        ('background:#111', 'background:#0d6efd'),
        ('background-color: #1a1a1a', 'background-color: #ffffff'),
        ('background-color: rgb(26, 26, 26)', 'background-color: #ffffff'),
        ('background: rgba(17, 17, 17, 0.98)', 'background: #ffffff'),
        ('background: rgba(10, 10, 10, 0.98)', 'background: #ffffff'),
        ('background: #0a0a0a', 'background: #ffffff'),
        ('background: rgba(0, 0, 0, 0.8)', 'background: #ffffff'),
        ('background-color: #0d6efd0d', 'background-color: rgba(13, 110, 253, 0.05)'), # Fix for rgba in hex-like format if any
    ]
    for old, new in bg_replacements:
        content = content.replace(old, new)

    # 2. FIX: Buttons specifically
    content = content.replace('background-color: #111;', 'background-color: #0d6efd;')
    content = content.replace('background-color: #111111;', 'background-color: #0d6efd;')
    content = content.replace('background-color: #222;', 'background-color: #0d6efd;')

    # 3. Text Color Replacements (#111111)
    text_replacements = [
        ('color: #eee', 'color: #111111'),
        ('color: #ddd', 'color: #111111'),
        ('color: #ccc', 'color: #6c757d'),
        ('color: #bbb', 'color: #6c757d'),
        ('color: #fff', 'color: #111111'),
        ('color: #ffffff', 'color: #111111'),
        ('color: rgba(255, 255, 255, 0.7)', 'color: #6c757d'),
        ('color: rgba(255, 255, 255, 0.5)', 'color: #9ca3af'),
    ]
    for old, new in text_replacements:
        content = content.replace(old, new)

    # 4. Restore White/Status Colors
    restore_white = [
        ('background-color: #0d6efd; color: #111111', 'background-color: #0d6efd; color: #ffffff'),
        ('background: #0d6efd; color: #111111', 'background: #0d6efd; color: #ffffff'),
        ('background-color: #dc3545; color: #111111', 'background-color: #dc3545; color: #ffffff'),
        ('background-color: #2ecc71; color: #111111', 'background-color: #2ecc71; color: #ffffff'),
        ('background-color: #e74c3c; color: #111111', 'background-color: #e74c3c; color: #ffffff'),
        ('color: #fff; background-color: #111', 'color: #ffffff; background-color: #0d6efd'), # Catch this pattern
        ('color: #fff; background-color: #0d6efd', 'color: #ffffff; background-color: #0d6efd'),
        ('color: #fff; background: #0d6efd', 'color: #ffffff; background: #0d6efd'),
    ]
    for old, new in restore_white:
        content = content.replace(old, new)

    # 5. Fix Broken Hex Codes
    content = content.replace('#111ffffff', '#ffffff')
    content = content.replace('#111fff', '#ffffff')

    # 6. Normalize Headers to Primary Blue
    header_patterns = [r'<h[1-6][^>]*style="[^"]*color:\s*#111111', r'<h[1-6][^>]*style="[^"]*color:\s*#6c757d']
    for pattern in header_patterns:
        content = re.sub(pattern, lambda m: m.group(0).replace('#111111', '#0d6efd').replace('#6c757d', '#0d6efd'), content)

    # 7. Remove Shadows and Dark Overlays
    content = content.replace('text-shadow: 0 0 20px rgba(var(--lx-sky-rgb), 0.4);', 'text-shadow: none;')
    content = content.replace('text-shadow: 0 0 20px #dee2e6;', 'text-shadow: none;')
    content = content.replace('box-shadow: 0 8px 40px rgba(0, 0, 0, 0.5);', 'box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);')
    content = content.replace('box-shadow: 0 8px 40px rgba(0, 0, 0, 0.6);', 'box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);')
    content = content.replace('rgba(0, 0, 0, 0.5) 0px 4px 20px', 'rgba(0, 0, 0, 0.05) 0px 4px 12px')

    # 8. Video/Particle Background Removal
    content = re.sub(r'background-image:\s*url\("[^"]*particles[^"]*"\);', 'background: #ffffff;', content)
    content = re.sub(r'background-image:\s*url\("[^"]*abstract[^"]*"\);', 'background: #ffffff;', content)

    # 9. Legacy Token Mapping in CSS
    if file_path.endswith('.css'):
        content = content.replace('--lx-sky: #1ab2ff;', '--lx-sky: #0d6efd;')
        content = content.replace('--lx-sky-rgb: 77, 210, 255;', '--lx-sky-rgb: 13, 110, 253;')
        content = content.replace('--lx-text: #fff;', '--lx-text: #111111;')
        content = content.replace('--bg: #000;', '--bg: #f8f9fa;')
        
        # Ensure user message in CSS is blue
        content = content.replace('.message.user { background: linear-gradient(135deg, #111111 0%, #0d6efd 100%); color: #111111;', '.message.user { background: #0d6efd; color: #ffffff;')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

target_dirs = ['VICP_Attorney_Fees', 'VICP_Prediction', 'Vehicle_loss_Analyzer', 'VerdictIQ']
root_dir = r'c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel'

for d in target_dirs:
    dir_path = os.path.join(root_dir, d)
    if os.path.exists(dir_path):
        for file in os.listdir(dir_path):
            if file.endswith(('.html', '.css')):
                normalize_panel(os.path.join(dir_path, file))

print('Standardized design for requested panels.')
