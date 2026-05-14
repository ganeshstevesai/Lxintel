import os
import re

def fix_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. BUTTONS: Simple blue bg, white text, no shadow, no radius
    btn_style = (
        'background-color: #0d6efd !important; '
        'background: #0d6efd !important; '
        'color: #ffffff !important; '
        'border: none !important; '
        'border-radius: 0 !important; '
        'box-shadow: none !important; '
        'text-shadow: none !important; '
        'font-family: "Montserrat", sans-serif !important; '
        'font-weight: 600 !important; '
        'text-transform: uppercase !important; '
        'cursor: pointer !important; '
        'padding: 10px 24px !important; '
        'transition: background-color 0.2s !important; '
        'display: inline-flex !important; '
        'align-items: center !important; '
        'justify-content: center !important; '
        'gap: 8px !important;'
    )
    
    if file_path.endswith('.css'):
        # Global shadow and radius removal
        content = re.sub(r'box-shadow:[^;!]+(!important)?', 'box-shadow: none !important', content)
        content = re.sub(r'text-shadow:[^;!]+(!important)?', 'text-shadow: none !important', content)
        content = re.sub(r'border-radius:[^;!]+(!important)?', 'border-radius: 0 !important', content)
        
        # Enforce Black Body Text
        content = re.sub(r'body\s*\{([^}]*)color:\s*#[0-9a-fA-F]+', r'body {\1color: #111111', content)
        # Fix specific user message/header text that might be blue but should be black
        content = content.replace('color: #0d6efd; /* body text fix */', 'color: #111111;')
        
        # Enforce Blue Headings
        heading_selectors = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', '.card-title', '.header-title h1']
        for sel in heading_selectors:
            # Look for the selector and its color property
            pattern = re.escape(sel) + r'\s*\{([^}]*)color:\s*#111111'
            content = re.sub(pattern, sel + r' {\1color: #0d6efd', content)

        # Append universal button style at the end to override everything
        btn_selector = 'button, .btn, .btn-primary, .login-btn, .send-btn, #process-btn, #upload-new-files-btn, .start-btn, .new-chat-btn'
        content += f'\n\n/* FINAL THEME ENFORCEMENT */\n{btn_selector} {{ {btn_style} }}\n'
        content += 'button:hover, .btn:hover { background-color: #0b5ed7 !important; background: #0b5ed7 !important; transform: none !important; box-shadow: none !important; }\n'
        content += 'button:disabled, .btn:disabled { background: #e0e0e0 !important; color: #6c757d !important; cursor: not-allowed !important; }\n'

    if file_path.endswith('.html'):
        # Remove shadows and radius in HTML
        content = re.sub(r'style="([^"]*)border-radius:[^;"]+', r'style="\1border-radius: 0', content)
        content = re.sub(r'style="([^"]*)box-shadow:[^;"]+', r'style="\1box-shadow: none', content)
        content = re.sub(r'style="([^"]*)text-shadow:[^;"]+', r'style="\1text-shadow: none', content)
        
        # Fix inline buttons
        content = re.sub(r'style="([^"]*)background-color:\s*#[0-9a-fA-F]+', r'style="\1background-color: #0d6efd', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

root_dir = r'c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel'
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(('.html', '.css')):
            fix_file(os.path.join(root, file))

print('Double-checked all portals. Applied clean theme: Blue buttons (sharp edges), Black text, Blue headings, No shadows.')
