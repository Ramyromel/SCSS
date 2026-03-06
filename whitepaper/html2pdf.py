import pdfkit

# تأكد أن HTML موجود
input_html = "SCSS_Whitepaper.html"
output_pdf = "SCSS_Whitepaper.pdf"

try:
    pdfkit.from_file(input_html, output_pdf)
    print("PDF generated successfully!")
except Exception as e:
    print("Error:", e)
