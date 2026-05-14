import os
import re

css_files = [
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\static\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\settlement\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\Medical summary\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\injury\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\FAA_Medcert\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\Demand QA\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\demand Optimizer\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\casevalue\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\book_builder\index.css",
]

# Blues to replace:
replacements = [
    (r'(?i)#4dd2ff', '#0d6efd'),
    (r'(?i)#1ab2ff', '#0d6efd'),
    (r'(?i)#0b5ed7', '#0d6efd'),
    (r'(?i)#80dfff', '#0d6efd'),
    (r'(?i)#33ccff', '#0d6efd'),
    (r'(?i)#1ca8dd', '#0d6efd'),
    (r'(?i)#3498db', '#0d6efd'),
    (r'(?i)#8ae0ff', '#0d6efd'),
    (r'rgba\(77,\s*210,\s*255', 'rgba(13, 110, 253'),
]

for file in css_files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        for pat, repl in replacements:
            content = re.sub(pat, repl, content)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
print("Updated all blues to #0d6efd")
