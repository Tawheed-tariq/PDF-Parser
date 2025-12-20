


## Demo
<img src="https://github.com/CBIhalsen/PolyglotPDF/blob/main/static/demo.gif?raw=true" width="80%" height="40%">

### [🎬 Watch Full Video](https://github.com/CBIhalsen/PolyglotPDF/blob/main/demo.mp4)
 llms has been added as the translation api of choice, Doubao ,Qwen ,deepseek v3 , gpt4-o-mini are recommended. The color space error can be resolved by filling the white areas in PDF files. The old text to text translation api has been removed.

In addition, consider adding arxiv search function and rendering arxiv papers after latex translation.

### Pages show
<div style="display: flex; margin-bottom: 20px;">
    <img src="https://github.com/CBIhalsen/PolyglotPDF/blob/main/static/page1.png?raw=true" width="40%" height="20%" style="margin-right: 20px;">
    <img src="https://github.com/CBIhalsen/PolyglotPDF/blob/main/static/page2.jpeg?raw=true" width="40%" height="20%">
</div>
<div style="display: flex;">
    <img src="https://github.com/CBIhalsen/PolyglotPDF/blob/main/static/page3.png?raw=true" width="40%" height="20%" style="margin-right: 20px;">
    <img src="https://github.com/CBIhalsen/PolyglotPDF/blob/main/static/page4.png?raw=true" width="40%" height="20%">
</div>


# LLM API Application

## 302.AI
AI service aggregation platform supporting multiple international mainstream AI models:
- Official Website: [302.AI](https://302.ai)
- Registration: [Sign up with invitation link](https://share.302.ai/JBmCb1) (Use invitation code `JBmCb1` to get $1 bonus)
- Available Models: GPT-4o, GPT-4o-mini, Claude-3.7-Sonnet, DeepSeek-V3 and more
- Features: Access multiple AI models with one account, pay-per-use pricing

## Doubao & Deepseek
Apply through Volcengine platform:
- Application URL: [Volcengine-Doubao](https://www.volcengine.com/product/doubao/)
- Available Models: Doubao, Deepseek series models

## Tongyi Qwen
Apply through Alibaba Cloud platform:
- Application URL: [Alibaba Cloud-Tongyi Qwen](https://cn.aliyun.com/product/tongyi?from_alibabacloud=&utm_content=se_1019997984)
- Available Models: Qwen-Max, Qwen-Plus series models


## Overview
PolyglotPDF is an advanced PDF processing tool that employs specialized techniques for ultra-fast text, table, and formula recognition in PDF documents, typically completing processing within 1 second. It features OCR capabilities and layout-preserving translation, with full document translations usually completed within 10 seconds (speed may vary depending on the translation API provider).


## Features
- **Ultra-Fast Recognition**: Processes text, tables, and formulas in PDFs within ~1 second
- **Layout-Preserving Translation**: Maintains original document formatting while translating content
- **OCR Support**: Handles scanned documents efficiently
- **Text-based PDF**：No GPU required
- **Quick Translation**: Complete PDF translation in approximately 10 seconds
- **Flexible API Integration**: Compatible with various translation service providers
- **Web-based Comparison Interface**: Side-by-side comparison of original and translated documents
- **Enhanced OCR Capabilities**: Improved accuracy in text recognition and processing
- **Support for offline translation**: Use smaller translation model

## Installation and Usage

<details>
  <summary>Standard Installation</summary>

1. Clone the repository:
```bash
git clone https://github.com/CBIhalsen/PolyglotPDF.git
cd polyglotpdf
```

2. Install required packages:
```bash
pip install -r requirements.txt
```
3. Configure your API key in config.json. The alicloud translation API is not recommended.

4. Run the application:
```bash
python app.py
```

5. Access the web interface:
Open your browser and navigate to `http://127.0.0.1:8000`
</details>

<details>
  <summary>Docker Installation</summary>

## Quick Start Without Persistence

If you want to quickly test PolyglotPDF without setting up persistent directories:

```bash
# Pull the image first
docker pull 2207397265/polyglotpdf:latest

# Run container without mounting volumes (data will be lost when container is removed)
docker run -d -p 12226:12226 --name polyglotpdf 2207397265/polyglotpdf:latest
```

This is the fastest way to try PolyglotPDF, but all uploaded PDFs and configuration changes will be lost when the container stops.

## Installation with Persistent Storage

```bash
# Create necessary directories
mkdir -p config fonts static/original static/target static/merged_pdf

# Create config file
nano config/config.json    # or use any text editor
# Copy configuration template from the project into this file
# Make sure to fill in your API keys and other configuration details

# Set permissions
chmod -R 755 config fonts static
```

### Quick Start

Use the following commands to pull and run the PolyglotPDF Docker image:

```bash
# Pull image
docker pull 2207397265/polyglotpdf:latest

# Run container
docker run -d -p 12226:12226 --name polyglotpdf \
  -v ./config/config.json:/app/config.json \
  -v ./fonts:/app/fonts \
  -v ./static/original:/app/static/original \
  -v ./static/target:/app/static/target \
  -v ./static/merged_pdf:/app/static/merged_pdf \
  2207397265/polyglotpdf:latest
```

### Access the Application

After the container starts, open in your browser:
```
http://localhost:12226
```

### Using Docker Compose

Create a `docker-compose.yml` file:

```yaml
version: '3'
services:
  polyglotpdf:
    image: 2207397265/polyglotpdf:latest
    ports:
      - "12226:12226"
    volumes:
      - ./config.json:/app/config.json # Configuration file
      - ./fonts:/app/fonts # Font files
      - ./static/original:/app/static/original # Original PDFs
      - ./static/target:/app/static/target # Translated PDFs
      - ./static/merged_pdf:/app/static/merged_pdf # Merged PDFs
    restart: unless-stopped
```

Then run:

```bash
docker-compose up -d
```

### Common Docker Commands

```bash
# Stop container
docker stop polyglotpdf

# Restart container
docker restart polyglotpdf

# View logs
docker logs polyglotpdf
```
</details>

## Requirements
- Python 3.8+
- deepl==1.17.0
- Flask==2.0.1
- Flask-Cors==5.0.0
- langdetect==1.0.9
- Pillow==10.2.0
- PyMuPDF==1.24.0
- pytesseract==0.3.10
- requests==2.31.0
- tiktoken==0.6.0
- Werkzeug==2.0.1

## Acknowledgments
This project leverages PyMuPDF's capabilities for efficient PDF processing and layout preservation.

## Upcoming Improvements
- PDF chat functionality
- Academic PDF search integration
- Optimization for even faster processing speeds

### Known Issues
- **Issue Description**: Error during text re-editing: `code=4: only Gray, RGB, and CMYK colorspaces supported`
- **Symptom**: Unsupported color space encountered during text block editing
- **Current Workaround**: Skip text blocks with unsupported color spaces
- **Proposed Solution**: Switch to OCR mode for entire pages containing unsupported color spaces
- **Example**: [View PDF sample with unsupported color spaces](https://github.com/CBIhalsen/PolyglotPDF/blob/main/static/colorspace_issue_sample.pdf)

### TODO
- □ **Custom Terminology Database**: Support custom terminology databases with prompts for domain-specific professional translation
- □ **AI Reflow Feature**: Convert double-column PDFs to single-column HTML blog format for easier reading on mobile devices
- □ **Multi-format Export**: Export translation results to PDF, HTML, Markdown and other formats
- □ **Multi-device Synchronization**: Read translations on mobile after processing on desktop
- □ **Enhanced Merge Logic**: Improve the current merge logic by disabling font name detection and enabling horizontal, vertical, x, y range overlap merging

### Font Optimization
Current font configuration in the `start` function of `main.py`:
```python
# Current configuration
css=f"* {{font-family:{get_font_by_language(self.target_language)};font-size:auto;color: #111111 ;font-weight:normal;}}"
```

You can optimize font display through the following methods:

1. **Modify Default Font Configuration**
```python
# Custom font styles
css=f"""* {{
    font-family: {get_font_by_language(self.target_language)};
    font-size: auto;
    color: #111111;
    font-weight: normal;
    letter-spacing: 0.5px;  # Adjust letter spacing
    line-height: 1.5;      # Adjust line height
}}"""
```

2. **Embed Custom Fonts**
You can embed custom fonts by following these steps:
- Place font files (.ttf, .otf) in the project's `fonts` directory
- Use `@font-face` to declare custom fonts in CSS
```python
css=f"""
@font-face {{
    font-family: 'CustomFont';
    src: url('fonts/your-font.ttf') format('truetype');
}}
* {{
    font-family: 'CustomFont', {get_font_by_language(self.target_language)};
    font-size: auto;
    font-weight: normal;
}}
"""
```

### Basic Principles
This project follows similar basic principles as Adobe Acrobat DC's PDF editing, using PyMuPDF for text block recognition and manipulation:

- **Core Process**:
```python
# Get text blocks from the page
blocks = page.get_text("dict")["blocks"]

# Process each text block
for block in blocks:
    if block.get("type") == 0:  # text block
        bbox = block["bbox"]     # get text block boundary
        text = ""
        font_info = None
        # Collect text and font information
        for line in block["lines"]:
            for span in line["spans"]:
                text += span["text"] + " "
```
This approach directly processes PDF text blocks, maintaining the original layout while achieving efficient text extraction and modification.

- **Technical Choices**:
  - Utilizes PyMuPDF for PDF parsing and editing
  - Focuses on text processing
  - Avoids complex operations like AI formula recognition, table processing, or page restructuring

- **Why Avoid Complex Processing**:
  - AI recognition of formulas, tables, and PDF restructuring faces severe performance bottlenecks
  - Complex AI processing leads to high computational costs
  - Significantly increased processing time (potentially tens of seconds or more)
  - Difficult to deploy at scale with low costs in production environments
  - Not suitable for online services requiring quick response times

- **Project Scope**:
  - This project only serves to demonstrate the correct approach for layout-preserved PDF translation and AI-assisted PDF reading. Converting PDF files to markdown format for large language models to read, in my opinion, is not a wise approach.
  - Aims for optimal performance-to-cost ratio

- **Performance**:
  - PolyglotPDF API response time: ~1 second per page
  - Low computational resource requirements, suitable for scale deployment
  - High cost-effectiveness for commercial applications

- * Contact author:
QQ： 1421243966
email: 1421243966@qq.com

Related questions answered and discussed：

 QQ group:
 1031477425

