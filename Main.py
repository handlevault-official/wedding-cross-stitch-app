import io
import math
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import streamlit as st

# ==============================================================================
# 1. STREAMLIT PAGE CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="Sovereign Cross Stitch Studio",
    page_icon="🧵",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==============================================================================
# 2. AUTHENTIC DMC COLOR PALETTE DATABASE
# ==============================================================================
# Curated DMC stranded cotton thread database with calibrated RGB values & symbols
DMC_PALETTE = [
    # Whites, Creams & Ivories
    {"code": "B5200", "name": "Bright Snow White", "hex": "#FFFFFF", "r": 255, "g": 255, "b": 255, "sym": "◇"},
    {"code": "Blanc", "name": "White", "hex": "#FBFBFB", "r": 251, "g": 251, "b": 251, "sym": "□"},
    {"code": "Ecru", "name": "Ecru Silk", "hex": "#F3EFE3", "r": 243, "g": 239, "b": 227, "sym": "○"},
    {"code": "3865", "name": "Winter White", "hex": "#F7F6F2", "r": 247, "g": 246, "b": 242, "sym": "△"},
    {"code": "712", "name": "Cream", "hex": "#F3EDDA", "r": 243, "g": 237, "b": 218, "sym": "▽"},
    {"code": "739", "name": "Tan Ultra Very Light", "hex": "#E7DEC7", "r": 231, "g": 222, "b": 199, "sym": "◬"},
    {"code": "738", "name": "Tan Very Light", "hex": "#D8CCA7", "r": 216, "g": 204, "b": 167, "sym": "⬡"},
    
    # Blushes, Pinks & Roses
    {"code": "948", "name": "Peach Very Light", "hex": "#FEECE6", "r": 254, "g": 236, "b": 230, "sym": "♡"},
    {"code": "754", "name": "Peach Light", "hex": "#F7D6CB", "r": 247, "g": 214, "b": 203, "sym": "♥"},
    {"code": "3778", "name": "Terra Cotta Light", "hex": "#D88E7B", "r": 216, "g": 142, "b": 123, "sym": "♠"},
    {"code": "3689", "name": "Mauve Light", "hex": "#F7D7DF", "r": 247, "g": 215, "b": 223, "sym": "✿"},
    {"code": "3688", "name": "Mauve Medium", "hex": "#E8A7B8", "r": 232, "g": 167, "b": 184, "sym": "❀"},
    {"code": "3687", "name": "Mauve", "hex": "#C46D82", "r": 196, "g": 109, "b": 130, "sym": "❁"},
    {"code": "224", "name": "Shell Pink Very Light", "hex": "#E6C6C1", "r": 230, "g": 198, "b": 193, "sym": "✦"},
    {"code": "223", "name": "Shell Pink Light", "hex": "#CB8C84", "r": 203, "g": 140, "b": 132, "sym": "✧"},
    {"code": "221", "name": "Shell Pink Dark", "hex": "#873B43", "r": 135, "g": 59, "b": 67, "sym": "★"},
    {"code": "818", "name": "Baby Pink", "hex": "#FFDFE5", "r": 255, "g": 223, "b": 229, "sym": "✶"},
    
    # Deep Reds & Burgundies
    {"code": "816", "name": "Garnet", "hex": "#941B2E", "r": 148, "g": 27, "b": 46, "sym": "▲"},
    {"code": "815", "name": "Garnet Medium", "hex": "#7E1324", "r": 126, "g": 19, "b": 36, "sym": "▼"},
    {"code": "814", "name": "Garnet Dark", "hex": "#630D1C", "r": 99, "g": 13, "b": 28, "sym": "◀"},
    {"code": "498", "name": "Red Dark", "hex": "#A7142A", "r": 167, "g": 20, "b": 42, "sym": "◆"},
    {"code": "321", "name": "Red", "hex": "#C71B32", "r": 199, "g": 27, "b": 50, "sym": "◈"},
    
    # Golds, Champagnes & Warm Ochres
    {"code": "677", "name": "Old Gold Very Light", "hex": "#F0E5BE", "r": 240, "g": 229, "b": 190, "sym": "⬢"},
    {"code": "676", "name": "Old Gold Light", "hex": "#DECB95", "r": 222, "g": 203, "b": 149, "sym": "⬣"},
    {"code": "729", "name": "Old Gold Medium", "hex": "#C29F55", "r": 194, "g": 159, "b": 85, "sym": "⊕"},
    {"code": "680", "name": "Old Gold Dark", "hex": "#A88034", "r": 168, "g": 128, "b": 52, "sym": "⊖"},
    {"code": "3829", "name": "Old Gold Very Dark", "hex": "#99732B", "r": 153, "g": 115, "b": 43, "sym": "⊗"},
    {"code": "745", "name": "Yellow Pale Light", "hex": "#FBE8A4", "r": 251, "g": 232, "b": 164, "sym": "⊘"},
    {"code": "743", "name": "Yellow Medium", "hex": "#FED352", "r": 254, "g": 211, "b": 82, "sym": "⊙"},
    
    # Botanical Greens & Foliage
    {"code": "524", "name": "Fern Green Very Light", "hex": "#C2C9AC", "r": 194, "g": 201, "b": 172, "sym": "♣"},
    {"code": "523", "name": "Fern Green Light", "hex": "#A5AE8B", "r": 165, "g": 174, "b": 139, "sym": "♧"},
    {"code": "522", "name": "Fern Green", "hex": "#87926C", "r": 135, "g": 146, "b": 108, "sym": "✕"},
    {"code": "520", "name": "Fern Green Dark", "hex": "#586541", "r": 88, "g": 101, "b": 65, "sym": "✖"},
    {"code": "3051", "name": "Green Gray Dark", "hex": "#515B38", "r": 81, "g": 91, "b": 56, "sym": "✛"},
    {"code": "3348", "name": "Yellow Green Light", "hex": "#CCD98B", "r": 204, "g": 217, "b": 139, "sym": "♁"},
    {"code": "3346", "name": "Hunter Green", "hex": "#406C32", "r": 64, "g": 108, "b": 50, "sym": "⚙"},
    {"code": "895", "name": "Hunter Green Very Dark", "hex": "#1C3E17", "r": 28, "g": 62, "b": 23, "sym": "■"},
    
    # Classic Blues, Navies & Lavenders
    {"code": "828", "name": "Blue Ultra Very Light", "hex": "#C5E8ED", "r": 197, "g": 232, "b": 237, "sym": "☾"},
    {"code": "826", "name": "Blue Medium", "hex": "#6B9EC7", "r": 107, "g": 158, "b": 199, "sym": "☽"},
    {"code": "824", "name": "Blue Very Dark", "hex": "#2B587D", "r": 43, "g": 88, "b": 125, "sym": "☂"},
    {"code": "939", "name": "Navy Blue Very Dark", "hex": "#1B2333", "r": 27, "g": 35, "b": 51, "sym": "⚓"},
    {"code": "209", "name": "Lavender Dark", "hex": "#A274A4", "r": 162, "g": 116, "b": 164, "sym": "♪"},
    {"code": "550", "name": "Violet Very Dark", "hex": "#5C1758", "r": 92, "g": 23, "b": 88, "sym": "♫"},
    
    # Earth Browns, Grays & Charcoal
    {"code": "437", "name": "Tan Light", "hex": "#E4BB8F", "r": 228, "g": 187, "b": 143, "sym": "☖"},
    {"code": "435", "name": "Brown Very Light", "hex": "#B87B4B", "r": 184, "g": 123, "b": 75, "sym": "☗"},
    {"code": "433", "name": "Brown Medium", "hex": "#764322", "r": 118, "g": 67, "b": 34, "sym": "☁"},
    {"code": "898", "name": "Coffee Brown Very Dark", "hex": "#492A13", "r": 73, "g": 42, "b": 19, "sym": "⚡"},
    {"code": "3371", "name": "Black Brown", "hex": "#1E120A", "r": 30, "g": 18, "b": 10, "sym": "♠"},
    {"code": "415", "name": "Pearl Gray", "hex": "#D3D3D6", "r": 211, "g": 211, "b": 214, "sym": "✦"},
    {"code": "318", "name": "Steel Gray Light", "hex": "#ABABAB", "r": 171, "g": 171, "b": 171, "sym": "⊕"},
    {"code": "414", "name": "Steel Gray Dark", "hex": "#8C8C8C", "r": 140, "g": 140, "b": 140, "sym": "⊗"},
    {"code": "3799", "name": "Pewter Gray Very Dark", "hex": "#383838", "r": 56, "g": 56, "b": 56, "sym": "●"},
    {"code": "310", "name": "Black", "hex": "#000000", "r": 0, "g": 0, "b": 0, "sym": "■"},
]

# Precompute NumPy RGB array for vectorized matching
DMC_RGB_ARRAY = np.array([[c["r"], c["g"], c["b"]] for c in DMC_PALETTE], dtype=np.float32)

# ==============================================================================
# 3. COLOR MATCHING & IMAGE PROCESSING
# ==============================================================================
def find_closest_dmc_color(rgb_tuple):
    """
    Finds the closest authentic DMC floss color using human perceptual weights:
    sqrt(2*dR^2 + 4*dG^2 + 3*dB^2)
    """
    r, g, b = rgb_tuple[:3]
    dr = DMC_RGB_ARRAY[:, 0] - r
    dg = DMC_RGB_ARRAY[:, 1] - g
    db = DMC_RGB_ARRAY[:, 2] - b
    distances = (2.0 * (dr ** 2)) + (4.0 * (dg ** 2)) + (3.0 * (db ** 2))
    closest_idx = int(np.argmin(distances))
    return DMC_PALETTE[closest_idx]

def create_sample_wedding_image():
    """Generates an elegant sample image for demonstration."""
    img = Image.new("RGB", (400, 400), color=(250, 247, 242))
    draw = ImageDraw.Draw(img)
    # Interlocking golden rings
    draw.ellipse([100, 140, 240, 280], outline=(184, 142, 60), width=16)
    draw.ellipse([170, 140, 310, 280], outline=(216, 175, 90), width=16)
    # Botanical garland accents
    draw.arc([70, 100, 330, 320], start=30, end=150, fill=(88, 101, 65), width=6)
    draw.arc([70, 100, 330, 320], start=210, end=330, fill=(88, 101, 65), width=6)
    # Rose buds
    for x, y in [(90, 210), (310, 210), (140, 310), (260, 310), (200, 110)]:
        draw.ellipse([x - 12, y - 12, x + 12, y + 12], fill=(167, 20, 42))
    return img

def process_cross_stitch_pattern(image, target_width, max_colors):
    """
    Downsamples the input image, quantizes to the requested number of colors,
    and maps each pixel to the nearest authentic DMC thread palette entry.
    """
    # Calculate proportional height
    aspect = image.height / image.width
    target_height = max(10, int(round(target_width * aspect)))

    # Step 1: Smooth resize
    small_img = image.resize((target_width, target_height), Image.Resampling.LANCZOS)

    # Step 2: Adaptive color quantization
    quantized = small_img.convert("P", palette=Image.Palette.ADAPTIVE, colors=max_colors)
    quantized_rgb = quantized.convert("RGB")
    pixel_data = np.array(quantized_rgb)

    # Step 3: Map pixels to DMC palette & collect stitch statistics
    h, w, _ = pixel_data.shape
    dmc_grid = []
    color_counts = {}

    for y in range(h):
        row = []
        for x in range(w):
            rgb = tuple(pixel_data[y, x])
            dmc = find_closest_dmc_color(rgb)
            row.append(dmc)
            code = dmc["code"]
            color_counts[code] = color_counts.get(code, 0) + 1
        dmc_grid.append(row)

    total_stitches = w * h

    # Compile statistics DataFrame
    stats = []
    dmc_by_code = {c["code"]: c for c in DMC_PALETTE}
    for code, count in sorted(color_counts.items(), key=lambda item: item[1], reverse=True):
        info = dmc_by_code[code]
        pct = (count / total_stitches) * 100.0
        # 1 standard 8m DMC skein ≈ 1,800 stitches on 14-count Aida (2-strand)
        skeins = max(1, math.ceil(count / 1800.0))
        stats.append({
            "DMC Code": info["code"],
            "Color Name": info["name"],
            "Symbol": info["sym"],
            "Hex": info["hex"],
            "Stitch Count": count,
            "Percentage": f"{pct:.1f}%",
            "Skeins Needed": skeins,
        })

    df_stats = pd.DataFrame(stats)
    return w, h, dmc_grid, df_stats

def render_chart_preview(w, h, dmc_grid, cell_size=12, show_symbols=False):
    """
    Draws a cross-stitch chart with a 10x10 bold grid overlay and optional DMC symbols.
    """
    chart_w = w * cell_size
    chart_h = h * cell_size
    chart = Image.new("RGB", (chart_w, chart_h), color=(255, 255, 255))
    draw = ImageDraw.Draw(chart)

    # Fill cells with DMC colors
    for y in range(h):
        for x in range(w):
            dmc = dmc_grid[y][x]
            x0 = x * cell_size
            y0 = y * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size
            draw.rectangle([x0, y0, x1, y1], fill=(dmc["r"], dmc["g"], dmc["b"]))
            if show_symbols and cell_size >= 14:
                # Contrast symbol color
                lum = 0.299 * dmc["r"] + 0.587 * dmc["g"] + 0.114 * dmc["b"]
                sym_color = (0, 0, 0) if lum > 140 else (255, 255, 255)
                draw.text((x0 + 2, y0 + 1), dmc["sym"], fill=sym_color)

    # Draw standard cross-stitch grid lines
    # Light lines every 1 cell
    for x in range(0, chart_w + 1, cell_size):
        line_color = (150, 130, 110) if (x // cell_size) % 10 == 0 else (220, 215, 205)
        line_width = 2 if (x // cell_size) % 10 == 0 else 1
        draw.line([(x, 0), (x, chart_h)], fill=line_color, width=line_width)

    for y in range(0, chart_h + 1, cell_size):
        line_color = (150, 130, 110) if (y // cell_size) % 10 == 0 else (220, 215, 205)
        line_width = 2 if (y // cell_size) % 10 == 0 else 1
        draw.line([(0, y), (chart_w, y)], fill=line_color, width=line_width)

    return chart

# ==============================================================================
# 4. STREAMLIT APPLICATION UI
# ==============================================================================
st.markdown(
    """
    <div style="background-color: #2C2523; padding: 22px 28px; border-radius: 14px; margin-bottom: 24px; color: #FAF7F2; border-left: 6px solid #B88E3C;">
        <h1 style="margin: 0; font-family: serif; font-size: 32px; color: #F5F2EB;">🧵 Sovereign Cross Stitch Pattern Generator</h1>
        <p style="margin: 6px 0 0 0; font-size: 14px; color: #D4C3A3;">
            Wedding & Heirloom Keepsake Edition • Authentic DMC Floss Matcher • Multi-count Aida Cloth Sizing
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------- SIDEBAR CONTROLS -----------------
with st.sidebar:
    st.header("⚙️ Pattern Specifications")
    
    # Image source
    source_mode = st.radio(
        "Design Source",
        ["🖼️ Sample Wedding Heirloom (Demo)", "📤 Upload My Own Image"],
        index=0,
    )
    
    uploaded_file = None
    if source_mode == "📤 Upload My Own Image":
        uploaded_file = st.file_uploader(
            "Pumili ng Larawan (PNG, JPG, WEBP)",
            type=["png", "jpg", "jpeg", "webp"],
            help="Mag-upload ng portrait, wedding invite, monogram, o anumang disenyo.",
        )

    st.markdown("---")
    st.subheader("📐 Grid & Canvas Dimensions")
    
    stitch_width = st.slider(
        "Stitch Width (Lapad ng Grid sa Tahi)",
        min_value=40,
        max_value=300,
        value=120,
        step=5,
        help="Karaniwang beginner: 60-100 stitches; Intermediate/Heirloom: 120-200 stitches.",
    )

    max_colors = st.slider(
        "Maximum DMC Colors (Dami ng Kulay)",
        min_value=6,
        max_value=45,
        value=18,
        step=1,
        help="Mas maraming kulay = mas detalyado ngunit mas maraming skeins ang bibilhin.",
    )

    st.markdown("---")
    st.subheader("🪡 Aida Fabric Sizing")
    
    fabric_count = st.selectbox(
        "Aida Cloth Count",
        options=[11, 14, 16, 18, 22],
        index=1,
        help="14-count ang pinakapopular na standard para sa wedding keepsakes.",
    )

    st.markdown("---")
    st.subheader("🎨 View Settings")
    show_symbols = st.checkbox("Ipakita ang DMC Chart Symbols sa Grid", value=False)
    cell_render_size = st.slider("Preview Zoom / Cell Size (px)", min_value=6, max_value=22, value=10)

# ----------------- LOAD & PROCESS IMAGE -----------------
if uploaded_file is not None:
    try:
        input_image = Image.open(uploaded_file).convert("RGB")
    except Exception as e:
        st.error(f"Hindi mabasa ang larawan: {e}")
        st.stop()
else:
    input_image = create_sample_wedding_image()

# Process pattern
with st.spinner("Kinakalkula ang authentic DMC matching at fabric dimensions..."):
    w_stitches, h_stitches, dmc_grid, df_stats = process_cross_stitch_pattern(
        input_image, target_width=stitch_width, max_colors=max_colors
    )

# Physical Sizing Calculations
width_inches = w_stitches / fabric_count
height_inches = h_stitches / fabric_count
width_cm = width_inches * 2.54
height_cm = height_inches * 2.54
cut_w_inches = width_inches + 6.0  # +3" margin on each side for hoop framing
cut_h_inches = height_inches + 6.0
total_stitches = w_stitches * h_stitches
total_skeins = int(df_stats["Skeins Needed"].sum())
active_dmc_count = len(df_stats)

# ----------------- TOP METRIC TILES -----------------
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Grid Dimension", f"{w_stitches} × {h_stitches}", "Stitches")
col2.metric("Stitched Area", f"{width_inches:.1f}\" × {height_inches:.1f}\"", f"{width_cm:.1f} × {height_cm:.1f} cm")
col3.metric("Cut Fabric (+3\" Margin)", f"{cut_w_inches:.1f}\" × {cut_h_inches:.1f}\"", f"{fabric_count}-Count Aida")
col4.metric("DMC Floss Colors", f"{active_dmc_count} Colors", "Matched")
col5.metric("Total Skeins Needed", f"{total_skeins} Skeins", f"{total_stitches:,} Stitches")

st.markdown("---")

# ----------------- TABS: PATTERN, SHOPPING LIST & EXPORT -----------------
tab1, tab2, tab3 = st.tabs(["🖼️ Pattern Chart & Preview", "🧵 DMC Floss Shopping List", "📄 Export & Downloads"])

with tab1:
    col_l, col_r = st.columns([1, 2])
    
    with col_l:
        st.subheader("Original Image")
        st.image(input_image, caption="Uploaded / Source Design", use_container_width=True)
        
        st.info(
            f"💡 **Fabric Recommendation:**\n"
            f"- Gamitin ang **{fabric_count}-Count Aida Cloth**.\n"
            f"- Mag-cut ng tela na may sukat na **{cut_w_inches:.1f} × {cut_h_inches:.1f} inches** "
            f"upang magkaroon ng sapat na allowance para sa wooden embroidery hoop o frame."
        )

    with col_r:
        st.subheader("Cross Stitch Chart Output")
        chart_image = render_chart_preview(
            w_stitches, h_stitches, dmc_grid, cell_size=cell_render_size, show_symbols=show_symbols
        )
        st.image(
            chart_image,
            caption=f"DMC Pattern Chart ({w_stitches}w × {h_stitches}h stitches • 10×10 Bold Grid Lines)",
            use_container_width=True,
        )

with tab2:
    st.subheader("🧵 DMC Stranded Cotton Thread Palette & Shopping Key")
    st.write(
        "Ito ang kumpletong listahan ng mga kulay ng DMC thread na gagamitin, "
        "kabilang ang bilang ng tahi at dami ng 8-meter skeins na dapat bilhin."
    )
    
    # Styled table display
    st.dataframe(
        df_stats[["DMC Code", "Color Name", "Symbol", "Hex", "Stitch Count", "Percentage", "Skeins Needed"]],
        use_container_width=True,
        hide_index=True,
    )
    
    # Visual Palette Swatches
    st.markdown("#### Visual Swatches")
    swatch_cols = st.columns(6)
    for idx, row in df_stats.iterrows():
        c_idx = idx % 6
        with swatch_cols[c_idx]:
            st.markdown(
                f"""
                <div style="background-color: {row['Hex']}; height: 38px; border-radius: 6px; border: 1px solid #C0B7A8; display: flex; align-items: center; justify-content: center; font-weight: bold; color: {'#000' if row['Hex'] > '#888888' else '#FFF'};">
                    {row['Symbol']}
                </div>
                <div style="font-size: 12px; margin-top: 4px; font-weight: 600; text-align: center;">
                    DMC {row['DMC Code']}
                </div>
                <div style="font-size: 11px; color: #666; text-align: center; margin-bottom: 12px;">
                    {row['Stitch Count']} stitches
                </div>
                """,
                unsafe_allow_html=True,
            )

with tab3:
    st.subheader("📥 Export & Downloads")
    st.write("I-download ang mga file para sa iyong cross-stitch project:")
    
    down_col1, down_col2 = st.columns(2)
    
    # 1. Download High-Res PNG Chart
    with down_col1:
        st.markdown("#### 1. High-Resolution Pattern Image (PNG)")
        buf_img = io.BytesIO()
        chart_export = render_chart_preview(w_stitches, h_stitches, dmc_grid, cell_size=16, show_symbols=True)
        chart_export.save(buf_img, format="PNG")
        st.download_button(
            label="💾 I-download ang High-Res Pattern Chart (PNG)",
            data=buf_img.getvalue(),
            file_name=f"sovereign_cross_stitch_{w_stitches}x{h_stitches}.png",
            mime="image/png",
            use_container_width=True,
        )

    # 2. Download Floss CSV Shopping List
    with down_col2:
        st.markdown("#### 2. DMC Floss Shopping List (CSV)")
        csv_data = df_stats.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📋 I-download ang DMC Shopping Key (CSV)",
            data=csv_data,
            file_name=f"dmc_shopping_list_{w_stitches}x{h_stitches}.csv",
            mime="text/csv",
            use_container_width=True,
        )

# ----------------- FOOTER -----------------
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #8C8077; font-size: 12px; padding: 12px 0;">
        © 2026 Sovereign Cross Stitch Studio • Authentic DMC Floss Standard • Ready for Replit
    </div>
    """,
