import os
import re

def clean_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix specific broken patterns introduced by user or previous edits
    fix_replacements = [
        ('#111ffffff', '#ffffff'),
        ('#111fff', '#ffffff'), # This was also used for backgrounds
        ('box-: rgba(0, 0, 0, 0.05) 0px 4px 20px;', 'box-shadow: rgba(0, 0, 0, 0.05) 0px 4px 20px;'),
        ('box-: rgba(255, 255, 255, 0.5) 0px 4px 20px;', 'box-shadow: rgba(0, 0, 0, 0.05) 0px 4px 20px;'),
        ('color: #fffffffff;', 'color: #ffffff;'),
        ('color: #fffffffff', 'color: #ffffff'),
        ('background-color: #111ffffff', 'background-color: #ffffff'),
        ('background: rgba(0,0,0,0.2);', 'background: #f8f9fa;'), # Found in FAA_Medcert
        ('border-top: 1px solid rgba(77,210,255,0.1);', 'border-top: 1px solid #dee2e6;'),
        ('border-top: 1px solid rgba(255,255,255,0.05);', 'border-top: 1px solid #dee2e6;'),
        ('border: 1px solid rgba(13, 110, 253, 0.05);', 'border: 1px solid #dee2e6;'),
    ]

    for old, new in fix_replacements:
        content = content.replace(old, new)

    # 2. General Background replacements (Dark to Light)
    bg_replacements = [
        ('bg-[#0a0a0a]', 'bg-[#f8f9fa]'),
        ('bg-black', 'bg-white'),
        ('background-color: #1a1a1a', 'background-color: #ffffff'),
        ('background-color: #000', 'background-color: #ffffff'),
        ('background: rgba(17, 17, 17, 0.98)', 'background: #ffffff'),
        ('background: rgba(17, 17, 17, 0.95)', 'background: #ffffff'),
    ]

    for old, new in bg_replacements:
        content = content.replace(old, new)

    # 3. General Text color replacements
    text_replacements = [
        ('color: #eee', 'color: #111'),
        ('color: #ccc', 'color: #6c757d'),
        ('color: #eee;', 'color: #111111;'),
        ('color: #ccc;', 'color: #6c757d;'),
        ('color: #ccc !important', 'color: #6c757d !important'),
    ]

    for old, new in text_replacements:
        content = content.replace(old, new)

    # 4. Final safety for hex codes
    content = re.sub(r'#([0-9a-fA-F]{3}){3,}', lambda m: '#' + m.group(1)[:6] if len(m.group(0)) > 7 else m.group(0), content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

root_dir = r'c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel'
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(('.html', '.css')):
            clean_file(os.path.join(root, file))

print('Fixed broken styles and hex codes in all HTML and CSS files.')
