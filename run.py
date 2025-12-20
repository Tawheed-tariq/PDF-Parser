from main import main_function  # PolyglotPDF main_function

# 1. PDF file in the original folder
# pdf_filename = "/home/tawheed/Downloads/IS 42464.pdf"
pdf_filename = "/home/tawheed/Downloads/IS 4246.pdf"
# 2. Source and target languages
source_lang = "en-IN"
target_lang = "hi-IN"

# 3. Create processor
processor = main_function(
    pdf_path=pdf_filename,
    original_language=source_lang,
    target_language=target_lang
)

# 4. Run the main function
processor.main()

# 5. Check output PDF
output_pdf = f"{pdf_filename.rsplit('.',1)[0]}_{target_lang}.pdf"
print("Translated PDF saved at:", output_pdf)
