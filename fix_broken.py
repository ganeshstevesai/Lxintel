import os
import re

def fix_broken_css(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix long hex codes (9 characters like #111111fff)
    content = re.sub(r'#([0-9a-fA-F]{9})\b', '#ffffff', content)
    # Fix 8 characters
    content = re.sub(r'#([0-9a-fA-F]{8})\b', '#ffffff', content)
    # Fix specific broken ones
    content = content.replace('#111111fff', '#ffffff')
    content = content.replace('#111ffffff', '#ffffff')
    content = content.replace('#111fff', '#ffffff')
    
    # Fix broken attributes
    content = content.replace('box-:', 'box-shadow:')
    
    # Ensure user message text is white on blue
    if '.message.user' in content:
        content = re.sub(r'\.message\.user\s*\{([^}]*)color:\s*#[0-9a-fA-F]+', r'.message.user {\1color: #ffffff', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

root_dir = r'c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel'
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(('.html', '.css')):
            fix_broken_css(os.path.join(root, file))

print('Fixed broken CSS properties and hex codes.')
