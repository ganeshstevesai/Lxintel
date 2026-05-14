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

normalize_css = """
/* ====================================================
   GLOBAL NORMALIZATION - Consistent UI across panels
   ==================================================== */
body, html {
    font-family: "Montserrat", sans-serif !important;
    font-size: 14px !important;
    color: #111111 !important;
    background-color: #f8f9fa !important;
}
h1 { font-family: "Cormorant Garamond", serif !important; font-size: 2rem !important; font-weight: 700 !important; color: #0d6efd !important; text-shadow: none !important; }
h2 { font-family: "Cormorant Garamond", serif !important; font-size: 1.5rem !important; font-weight: 700 !important; color: #0d6efd !important; text-shadow: none !important; }
h3 { font-family: "Cormorant Garamond", serif !important; font-size: 1.2rem !important; font-weight: 600 !important; color: #0d6efd !important; text-shadow: none !important; }
h4, h5, h6 { font-family: "Cormorant Garamond", serif !important; font-size: 1rem !important; font-weight: 600 !important; color: #0d6efd !important; text-shadow: none !important; }
label, .form-label, .billing-label { font-family: "Montserrat", sans-serif !important; font-size: 13px !important; font-weight: 600 !important; color: #111111 !important; display: block !important; margin-bottom: 8px !important; }
p, li, td, th, span, div { font-family: "Montserrat", sans-serif !important; font-size: 14px !important; color: #111111; }
.logo, img.logo, .header-logo, .topbar-logo img, .app-header img, header img {
    filter: none !important; max-height: 48px !important; width: auto !important; object-fit: contain !important;
}
button, .btn, .btn-primary, .dark-theme-btn-primary, .login-btn, .send-btn, #process-btn, #upload-new-files-btn, .start-btn, .new-chat-btn {
    font-family: "Montserrat", sans-serif !important; font-size: 13px !important; font-weight: 600 !important;
    letter-spacing: 0.8px !important; text-transform: uppercase !important; padding: 10px 24px !important;
    border-radius: 6px !important; background: linear-gradient(135deg, #0d6efd, #0b5ed7) !important;
    color: #ffffff !important; border: none !important; 
    box-shadow: none !important;
    cursor: pointer !important; transition: all 0.2s ease-in-out !important;
}

/* Icon Buttons Reset - Ensuring visibility */
#upload-btn, 
#templates-btn, 
#templates-btn-initial,
.upload-icon-btn,
.menu-icon-btn {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 8px !important;
    width: 44px !important;
    height: 44px !important;
    border-radius: 8px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    color: #0d6efd !important;
    transform: none !important;
}

#upload-btn:hover, #templates-btn:hover, #templates-btn-initial:hover {
    background: rgba(13, 110, 253, 0.1) !important;
}

button:hover:not(:disabled), .btn:hover:not(:disabled), .login-btn:hover:not(:disabled), #process-btn:hover {
    background: linear-gradient(135deg, #0b5ed7, #0a58ca) !important;
    box-shadow: none !important;
    transform: translateY(-2px) !important;
}
button:disabled, .btn:disabled { background: #e0e0e0 !important; color: #999 !important; box-shadow: none !important; cursor: not-allowed !important; transform: none !important; }
input[type="text"], input[type="email"], input[type="password"], input[type="file"], textarea, select, .form-control {
    font-family: "Montserrat", sans-serif !important; font-size: 14px !important;
    color: #111111 !important; background-color: #ffffff !important;
    border: 1.5px solid #dee2e6 !important; border-radius: 6px !important; padding: 10px 14px !important;
}
input::placeholder, textarea::placeholder { color: #9ca3af !important; font-size: 13px !important; }
input:focus, textarea:focus, select:focus, .form-control:focus {
    border-color: #0d6efd !important; box-shadow: none !important; outline: none !important;
}
.card, .glass-panel, .dark-theme-card, .login-form-card, .item-card, .selected-files-card, .glass-card {
    background: #ffffff !important; border: 1.5px solid #dee2e6 !important;
    border-radius: 10px !important; 
    box-shadow: none !important;
    color: #111111 !important;
}
.card-number, .card-icon, .card-title, .card-desc, .card-arrow, .grid > a.card > * {
    border: none !important; box-shadow: none !important; background: transparent !important;
}
.login-page-content { max-width: 480px !important; width: 100% !important; margin: 0 auto !important; padding: 2rem !important; }
.login-form-card { padding: 2rem !important; max-width: 480px !important; width: 100% !important; }
.login-form-card h2 { font-size: 1.6rem !important; }
.header-bar, .app-header { padding: 14px 24px !important; border-bottom: 1.5px solid #dee2e6 !important; background: #ffffff !important; box-shadow: none !important; }
.card-header { font-size: 14px !important; font-weight: 600 !important; padding: 12px 16px !important; border-bottom: 1px solid #dee2e6 !important; background: #f8f9fa !important; color: #111111 !important; border-radius: 10px 10px 0 0 !important; }
* { text-shadow: none !important; box-shadow: none !important; }
"""

for file in css_files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'/\* ={4,}\s*GLOBAL NORMALIZATION.*', '', content, flags=re.DOTALL)
        content = re.sub(r'/\* Global Font & Color Overrides \*/.*', '', content, flags=re.DOTALL)
        content = re.sub(r'/\* Card Design Overrides - Flat, clean border \*/.*', '', content, flags=re.DOTALL)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content.strip() + '\n\n' + normalize_css)

print("Done - Global normalization updated.")
