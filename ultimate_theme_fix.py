import os
import re

def fix_portal(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. BUTTONS: Standardize all buttons across portals
    # Simple blue bg (#0d6efd), White text (#ffffff), 0 radius, 0 shadow, 0 gradient
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
        'transition: none !important;' # Disable transitions to avoid flickers/gradients
    )
    
    hover_style = (
        'background-color: #0b5ed7 !important; '
        'background: #0b5ed7 !important; '
        'box-shadow: none !important; '
        'transform: none !important; '
        'border: none !important;'
    )

    if file_path.endswith('.css'):
        # Force body text to black
        content = re.sub(r'body,\s*html\s*\{([^}]*)color:\s*#0d6efd', r'body, html {\1color: #111111', content)
        content = re.sub(r'body\s*\{([^}]*)color:\s*#0d6efd', r'body {\1color: #111111', content)
        
        # Global shadow/radius removal
        content = re.sub(r'box-shadow:[^;!]+(!important)?', 'box-shadow: none !important', content)
        content = re.sub(r'border-radius:[^;!]+(!important)?', 'border-radius: 0 !important', content)
        content = re.sub(r'text-shadow:[^;!]+(!important)?', 'text-shadow: none !important', content)

        # Force Headings to blue
        for h in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', '.card-title', '.header-title h1']:
            pattern = re.escape(h) + r'\s*\{([^}]*)color:\s*#111111'
            content = re.sub(pattern, h + r' {\1color: #0d6efd', content)

        # Force buttons
        btn_selectors = [
            'button', '.btn', '.btn-primary', '.login-btn', '.send-btn', 
            '#process-btn', '#upload-new-files-btn', '.start-btn', '.new-chat-btn',
            '.dark-theme-btn-primary'
        ]
        
        # Append clean styles at the end
        content += f"\n\n/* ULTIMATE THEME ENFORCEMENT */\n"
        content += f"{', '.join(btn_selectors)} {{ {btn_style} }}\n"
        content += f"{', '.join([s+':hover' for s in btn_selectors])} {{ {hover_style} }}\n"
        content += f"{', '.join([s+':disabled' for s in btn_selectors])} {{ background: #e0e0e0 !important; color: #6c757d !important; cursor: not-allowed !important; opacity: 1 !important; }}\n"

    if file_path.endswith('.html'):
        # Remove dark mode artifacts
        content = content.replace('<div class="video-background"></div>', '')
        content = content.replace('<div class="overlay"></div>', '')
        
        # Fix inline styles
        content = re.sub(r'style="([^"]*)border-radius:[^;"]+', r'style="\1border-radius: 0', content)
        content = re.sub(r'style="([^"]*)box-shadow:[^;"]+', r'style="\1box-shadow: none', content)
        content = re.sub(r'style="([^"]*)text-shadow:[^;"]+', r'style="\1text-shadow: none', content)
        content = re.sub(r'class="text-\[#111111\]"', r'class="text-[#0d6efd]"', content) # CaseValue login header

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

root_dir = r'c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel'
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(('.html', '.css')):
            fix_portal(os.path.join(root, file))

print('Ultimate theme fix applied. No gradients, No shadows, No radius. Blue buttons, Blue headings, Black body text.')
