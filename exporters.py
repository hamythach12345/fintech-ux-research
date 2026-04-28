"""Helpers để export markdown sang docx và pdf."""
import io
import os
import re


def md_to_docx_bytes(md_content: str) -> bytes:
    """Convert markdown string sang docx bytes."""
    from docx import Document
    from docx.shared import Pt, RGBColor
    
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Calibri'
    style.font.size = Pt(11)
    
    for line in md_content.split("\n"):
        line = line.rstrip()
        if not line.strip():
            continue
        
        if line.startswith("# "):
            doc.add_heading(line[2:], level=0)
        elif line.startswith("## "):
            doc.add_heading(line[3:], level=1)
        elif line.startswith("### "):
            doc.add_heading(line[4:], level=2)
        elif line.startswith("#### "):
            doc.add_heading(line[5:], level=3)
        elif line.startswith("- ") or line.startswith("* "):
            doc.add_paragraph(line[2:], style='List Bullet')
        elif line.startswith(("1. ", "2. ", "3. ", "4. ", "5. ")):
            doc.add_paragraph(line[3:], style='List Number')
        elif line.startswith("> "):
            p = doc.add_paragraph(line[2:])
            if p.runs:
                p.runs[0].italic = True
                p.runs[0].font.color.rgb = RGBColor(0x5A, 0x5A, 0x5A)
        elif line.startswith("---"):
            doc.add_paragraph("─" * 50)
        else:
            doc.add_paragraph(line)
    
    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer.getvalue()


def md_to_pdf_bytes(md_content: str, title: str = "Research Report") -> bytes:
    """Convert markdown string sang pdf bytes (hỗ trợ tiếng Việt)."""
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.colors import HexColor
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    
    # Đăng ký font Unicode hỗ trợ tiếng Việt
    default_font = 'Helvetica'
    try:
        # Thử Windows fonts
        if os.path.exists('C:/Windows/Fonts/arial.ttf'):
            pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
            pdfmetrics.registerFont(TTFont('Arial-Bold', 'C:/Windows/Fonts/arialbd.ttf'))
            default_font = 'Arial'
        # Thử Linux fonts (Streamlit Cloud)
        elif os.path.exists('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'):
            pdfmetrics.registerFont(TTFont('DejaVu', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
            pdfmetrics.registerFont(TTFont('DejaVu-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
            default_font = 'DejaVu'
    except Exception:
        pass
    
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=A4,
        rightMargin=2*cm, leftMargin=2*cm,
        topMargin=2*cm, bottomMargin=2*cm
    )
    
    styles = getSampleStyleSheet()
    
    h1_style = ParagraphStyle(
        'CustomH1', parent=styles['Heading1'],
        fontName=default_font, fontSize=20,
        textColor=HexColor('#1a1a1a'), spaceAfter=14, spaceBefore=10
    )
    h2_style = ParagraphStyle(
        'CustomH2', parent=styles['Heading2'],
        fontName=default_font, fontSize=15,
        textColor=HexColor('#2563eb'), spaceAfter=10, spaceBefore=14
    )
    h3_style = ParagraphStyle(
        'CustomH3', parent=styles['Heading3'],
        fontName=default_font, fontSize=12,
        textColor=HexColor('#1f2937'), spaceAfter=8, spaceBefore=10
    )
    body_style = ParagraphStyle(
        'CustomBody', parent=styles['Normal'],
        fontName=default_font, fontSize=10,
        alignment=TA_LEFT, spaceAfter=6, leading=14
    )
    quote_style = ParagraphStyle(
        'Quote', parent=styles['Normal'],
        fontName=default_font, fontSize=10,
        textColor=HexColor('#6b7280'),
        leftIndent=20, rightIndent=20,
        spaceAfter=8, leading=14
    )
    
    story = []
    
    for line in md_content.split("\n"):
        line = line.rstrip()
        if not line.strip():
            story.append(Spacer(1, 4))
            continue
        
        safe_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        safe_line = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', safe_line)
        safe_line = re.sub(r'\*(.+?)\*', r'<i>\1</i>', safe_line)
        
        try:
            if line.startswith("# "):
                story.append(Paragraph(safe_line[2:], h1_style))
            elif line.startswith("## "):
                story.append(Paragraph(safe_line[3:], h2_style))
            elif line.startswith("### "):
                story.append(Paragraph(safe_line[4:], h3_style))
            elif line.startswith("- ") or line.startswith("* "):
                story.append(Paragraph("• " + safe_line[2:], body_style))
            elif line.startswith("> "):
                story.append(Paragraph(safe_line[2:], quote_style))
            elif line.startswith("---"):
                story.append(Spacer(1, 8))
            else:
                story.append(Paragraph(safe_line, body_style))
        except Exception:
            continue
    
    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()