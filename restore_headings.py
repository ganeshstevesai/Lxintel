import os
import re

def restore_headings(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. CSS Heading/Title Classes
    content = content.replace('color: #111111;', 'color: #0d6efd;') # Wait, this is too broad!
    # Let's be specific.
    
    # Reset specific classes back to theme blue
    blue_classes = [
        '.card-title',
        '.header-title h1',
        '.login-page-content h1',
        '.login-form-card h2',
        '.section-title',
        '.detail-title',
        '.modal-header h2',
        '.message.assistant h3',
        '.sidebar-header h2',
    ]
    
    for cls in blue_classes:
        # Look for the class and its color property
        pattern = re.escape(cls) + r'\s*\{([^}]*)color:\s*#111111'
        content = re.sub(pattern, cls + r' {\1color: #0d6efd', content)

    # 2. HTML Inline Styles for Headers
    content = re.sub(r'(<h[1-6][^>]*style="[^"]*color:\s*)#111111', r'\1#0d6efd', content, flags=re.IGNORECASE)
    
    # 3. Restore Blue for any spans that look like titles
    content = content.replace('class="header-title" style="color: #111111', 'class="header-title" style="color: #0d6efd')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

root_dir = r'c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel'
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(('.html', '.css')):
            restore_headings(os.path.join(root, file))

print('Restored blue color to all headings and titles.')
