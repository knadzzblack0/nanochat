#!/usr/bin/env python3
"""
Script to convert markdown file to PDF with proper formatting for scientific articles.
"""

import markdown
from weasyprint import HTML, CSS
from pathlib import Path

def convert_markdown_to_pdf(input_file, output_file=None):
    """
    Convert a markdown file to PDF with scientific formatting.
    
    Args:
        input_file: Path to the input markdown file
        output_file: Path to the output PDF file (optional)
    """
    # Read the markdown file
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert markdown to HTML with extensions for better formatting
    html_content = markdown.markdown(
        md_content,
        extensions=[
            'extra',           # Tables, footnotes, etc.
            'codehilite',      # Code highlighting
            'toc',             # Table of contents
            'sane_lists',      # Better list handling
            'nl2br',           # Newline to break
        ]
    )
    
    # Create a complete HTML document with CSS styling
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Artigo - Termodinâmica</title>
        <style>
            @page {{
                size: A4;
                margin: 2.5cm 2cm;
                @bottom-center {{
                    content: counter(page);
                    font-size: 10pt;
                    color: #666;
                }}
            }}
            
            body {{
                font-family: 'Georgia', 'Times New Roman', serif;
                font-size: 11pt;
                line-height: 1.6;
                color: #333;
                text-align: justify;
                hyphens: auto;
            }}
            
            h1 {{
                font-size: 18pt;
                font-weight: bold;
                margin-top: 24pt;
                margin-bottom: 12pt;
                text-align: center;
                page-break-after: avoid;
            }}
            
            h2 {{
                font-size: 14pt;
                font-weight: bold;
                margin-top: 18pt;
                margin-bottom: 10pt;
                page-break-after: avoid;
            }}
            
            h3 {{
                font-size: 12pt;
                font-weight: bold;
                margin-top: 14pt;
                margin-bottom: 8pt;
                page-break-after: avoid;
            }}
            
            h4 {{
                font-size: 11pt;
                font-weight: bold;
                margin-top: 12pt;
                margin-bottom: 6pt;
                page-break-after: avoid;
            }}
            
            p {{
                margin-bottom: 10pt;
                text-indent: 1.5em;
            }}
            
            /* First paragraph after heading should not be indented */
            h1 + p, h2 + p, h3 + p, h4 + p {{
                text-indent: 0;
            }}
            
            /* Tables */
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 15pt 0;
                font-size: 10pt;
                page-break-inside: avoid;
            }}
            
            th {{
                background-color: #f0f0f0;
                font-weight: bold;
                padding: 8pt;
                border: 1pt solid #999;
                text-align: center;
            }}
            
            td {{
                padding: 6pt 8pt;
                border: 1pt solid #ccc;
                text-align: center;
            }}
            
            /* Code blocks */
            pre {{
                background-color: #f5f5f5;
                border: 1pt solid #ddd;
                border-radius: 3pt;
                padding: 10pt;
                font-family: 'Courier New', monospace;
                font-size: 9pt;
                overflow-x: auto;
                page-break-inside: avoid;
                white-space: pre-wrap;
            }}
            
            code {{
                font-family: 'Courier New', monospace;
                font-size: 9pt;
                background-color: #f5f5f5;
                padding: 2pt 4pt;
                border-radius: 2pt;
            }}
            
            /* Lists */
            ul, ol {{
                margin-left: 20pt;
                margin-bottom: 10pt;
            }}
            
            li {{
                margin-bottom: 5pt;
            }}
            
            /* Blockquotes */
            blockquote {{
                margin: 15pt 30pt;
                padding: 10pt 15pt;
                border-left: 3pt solid #ccc;
                background-color: #f9f9f9;
                font-style: italic;
            }}
            
            /* Horizontal rules */
            hr {{
                border: none;
                border-top: 1pt solid #ccc;
                margin: 20pt 0;
            }}
            
            /* Strong and emphasis */
            strong {{
                font-weight: bold;
            }}
            
            em {{
                font-style: italic;
            }}
            
            /* Links */
            a {{
                color: #0066cc;
                text-decoration: none;
            }}
            
            /* Page breaks */
            .page-break {{
                page-break-after: always;
            }}
            
            /* Avoid breaking these elements */
            h1, h2, h3, h4, h5, h6 {{
                page-break-after: avoid;
            }}
            
            table, figure, img {{
                page-break-inside: avoid;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Determine output filename
    if output_file is None:
        input_path = Path(input_file)
        output_file = input_path.with_suffix('.pdf')
    
    # Convert HTML to PDF
    print(f"Converting {input_file} to PDF...")
    HTML(string=full_html).write_pdf(output_file)
    print(f"PDF successfully created: {output_file}")
    
    return output_file

if __name__ == "__main__":
    import sys
    
    # Get input file from command line or use default
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "artigo_termodinamica_calor_especifico.md"
    
    # Get output file from command line if provided
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Convert the file
    try:
        result = convert_markdown_to_pdf(input_file, output_file)
        print(f"\n✓ Conversion completed successfully!")
        print(f"  Output: {result}")
    except Exception as e:
        print(f"\n✗ Error during conversion: {e}")
        sys.exit(1)
