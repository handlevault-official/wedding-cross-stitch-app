import numpy as np
from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="Sovereign Cross Stitch Generator", layout="wide"
)

st.title("💍 Sovereign Cross Stitch Generator - Wedding Edition")
st.write(
    "I-upload ang larawan para ma-convert sa cross-stitch pattern at grid."
)

# Sidebar para sa mga settings
st.sidebar.header("Pattern Settings")
grid_size = st.sidebar.slider("Grid Resolution (Size)", 20, 100, 50)
threshold = st.sidebar.slider("Contrast Threshold", 0, 255, 128)

# File uploader para sa larawan
uploaded_file = st.file_uploader(
    "Pumili ng Wedding Image (JPG/PNG)", type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
  # Buksan ang larawan gamit ang PIL
  image = Image.open(uploaded_file)

  col1, col2 = st.columns(2)

  with col1:
    st.subheader("Original Image")
    st.image(image, use_column_width=True)

  with col2:
    st.subheader("Cross-Stitch Grid Preview")
    # I-resize ang image base sa grid size
    img_resized = image.resize((grid_size, grid_size)).convert("L")
    img_array = np.array(img_resized)

    # Gawing black and white grid
    binary_grid = (img_array > threshold).astype(int)
    st.write(binary_grid)

  st.success("Na-load at na-process na ang pattern nang matagumpay!")
else:
  st.info(
    "Mag-upload ng larawan sa itaas para magsimula ang pagbuo ng pattern."
  )
# import streamlit as stimport osfrom PIL import Imageimport mathimport random# --- PAGE CONFIGURATION ---st.set_page_config(page_title="Sovereign Cross Stitch Generator - Wedding Edition", page_icon="🧵", layout="centered")# --- SESSION STATE INITIALIZATION ---if "purchased_patterns" not in st.session_state: st.session_state["purchased_patterns"] = []# --- APP BRANDING ---st.markdown("# 🧵 Sovereign Cross Stitch Generator")st.markdown("### Wedding & Heirloom Edition (Commercial PDF Pattern Creator)")st.caption("Gawing professional multi-page cross-stitch pattern ang iyong wedding photos at designs!")# --- SIDEBAR: PRICING & COMMERCIAL UPGRADE ---with st.sidebar: st.header("💎 Commercial Licensing & Pricing") st.info("📦 Free Tier: Preview at 1-Page Sample Grid.\n\n🌟 PRO Wedding Bundle (₱499): Unlimited High-Res Multi-Page PDF Patterns + Full DMC Legend & 10x10 Grid Tiling.") if st.button("💳 Bumili ng Pro License (₱499 via GCash)"): st.session_state["show_checkout"] = True if st.session_state.get("show_checkout", False): st.warning("Magpadala ng ₱499 sa GCash: 09288212987") ref_input = st.text_input("Ilagay ang GCash Reference Number:") if st.button("I-verify ang Bayad"): if ref_input: st.session_state["purchased_patterns"].append("PRO_LIFETIME") st.session_state["show_checkout"] = False st.success("🎉 Tagumpay! Na-activate na ang iyong PRO Wedding License.") st.rerun() else: st.error("Paki-lagay ang reference number.") if "PRO_LIFETIME" in st.session_state["purchased_patterns"]: st.success("✅ PRO License Active")# --- MAIN APP: UPLOAD & CONFIGURATION ---st.markdown("---")st.subheader("1️⃣ Mag-upload o Pumili ng Wedding Design")upload_option = st.radio("Pumili ng paraan:", ["Mag-upload ng Wedding Photo", "Pumili mula sa Sample Wedding Templates"])selected_design_name = "Custom Wedding Upload"if upload_option == "Mag-upload ng Wedding Photo": uploaded_file = st.file_uploader("I-upload ang litrato (JPG, PNG)", type=["jpg", "jpeg", "png"]) if uploaded_file is not None: image = Image.open(uploaded_file) st.image(image, caption="Na-upload na Litrato", width=300)else: template_choice = st.selectbox("Pumili ng Template:", [ "Classic Wedding Rings & Florals (300x450 Stitches)", "Bridal Silhouette & Roses (200x300 Stitches)", "Mr & Mrs Floral Monogram (150x150 Stitches)" ]) selected_design_name = template_choicest.markdown("---")st.subheader("2️⃣ Pattern Specifications (1-Year Heirloom Scale)")col1, col2 = st.columns(2)with col1: grid_size = st.selectbox("Grid / Stitch Dimensions:", ["300 x 450 (1-Year Masterpiece)", "200 x 300 (Large Tapestry)", "150 x 150 (Medium Project)"])with col2: fabric_count = st.selectbox("AIDA Cloth Count:", ["14 Count (Standard)", "16 Count", "18 Count (Fine Detail)"])# --- GENERATE & DOWNLOAD LOGIC ---st.markdown("---")if st.button("✨ Bumuo ng Professional PDF Pattern", type="primary"): with st.spinner("Binubuo ang DMC Thread Legend at Multi-Page Grid..."): # Simulation ng generation st.success("🎉 Tagumpay! Handa na ang iyong Wedding Cross Stitch Pattern.") # Display Mock Details st.markdown(f"### 📋 Pattern Summary: {selected_design_name}") st.markdown("- Total Colors: 24 DMC Palette Colors") st.markdown("- Estimated Threads: 18 Skeins (8m standard)") st.markdown("- Grid Format: Multi-Page Booklet (5 Pages with 10x10 Bold Markers)") # Check kung may PRO access para sa libreng download o kung bibili is_pro_unlocked = "PRO_LIFETIME" in st.session_state["purchased_patterns"] if is_pro_unlocked: st.download_button( label="📥 I-download ang Buong PRO PDF Pattern (Multi-Page)", data=b"Mock PDF Binary Data for Wedding Pattern", file_name="Wedding_Masterpiece_CrossStitch_Pattern.pdf", mime="application/pdf" ) else: # Free preview download button o prompt para magbayad st.info("💡 Na-generate ang Free Sample Preview (Page 1). Para ma-download ang buong Multi-Page PRO PDF, mag-upgrade sa sidebar (₱499).") st.download_button( label="📥 I-download ang Free Preview PDF", data=b"Mock Free Preview PDF Data", file_name="Wedding_Preview_Sample.pdf", mime="application/pdf" )

src/data/dmcPalette.ts
src/utils/colorMatcher.ts
src/utils/pdfGenerator.ts
src/components/Header.tsx
src/components/CheckoutModal.tsx
src/components/DesignSelector.tsx
src/components/PatternConfigurator.tsx
src/components/StitchViewer.tsx
src/components/FlossLegendTable.tsx
src/components/PageOverviewMap.tsx
src/App.tsx
build
Built
# Create a calculator within the app that determines the final stitched dimensions of the cross stitch pattern.

src/components/FabricCalculator.tsx
src/App.tsx
src/components/PatternConfigurator.tsx
build
Built
# Add a numeric input field in the FabricCalculator component that allows users to specify an additional fabric margin (e.g., 2, 3, or 4 inches) to automatically calculate the total fabric piece size needed for framing.

src/components/FabricCalculator.tsx
build
Built
# Add a visual progress tracker component where users can mark individual stitches as 'complete' by clicking on them in the stitch viewer, and display a percentage completion bar in the summary card.

src/components/StitchProgressTracker.tsx
src/components/StitchViewer.tsx
src/App.tsx
build
Built
# Analyze the complexity of the generated pattern (e.g., number of colors, confetti stitching frequency) and add a 'Difficulty Rating' (Beginner, Intermediate, Masterpiece) to the summary card to help users manage their expectations for the project

src/utils/colorMatcher.ts
src/utils/pdfGenerator.ts
src/App.tsx
build
Built
# Create a 'Saved Designs' gallery in the application that allows users to store and revisit their previously generated patterns in localStorage, showing a thumbnail and basic project details for each.

src/components/SavedDesignsGallery.tsx
src/components/Header.tsx
src/App.tsx
build
Built
# Add a feature to export the pattern data in CSV or JSON format for advanced users who want to use the data in external embroidery software.

src/utils/exportData.ts
src/components/ExportDataModal.tsx
src/components/FlossLegendTable.tsx
src/App.tsx
build
Built
# Update the FabricCalculator component to accept the current market price per DMC skein, and display an estimated 'Total Project Cost' in the summary card to help users plan their budget.

src/components/FabricCalculator.tsx
src/App.tsx
build
Built
# Create a 'My Thread Stash' component where users can input the DMC floss colors they already own, and add an indicator in the FlossLegendTable to highlight which colors are missing from their current inventory.

src/utils/stashStorage.ts
src/components/MyThreadStash.tsx
src/components/FlossLegendTable.tsx
src/components/Header.tsx
src/App.tsx
build
Built
# Create a 'Print Preview' modal that simulates how the multi-page PDF pattern will look when printed, including page numbering and bleed margins, to give users a better idea of their final physical document structure.

src/components/PrintPreviewModal.tsx
src/components/PageOverviewMap.tsx
src/App.tsx
# Create a 'Share Pattern' feature that generates a shareable link or social media preview card for the current pattern's metadata so users can showcase their wedding designs.
# Add a 'Pin to Pinterest' button within the SharePattern feature to generate a high-quality preview image and a link specifically optimized for Pinterest boards.

src/components/SharePatternModal.tsx
src/App.tsx
build
Built
# Create a 'Manual Editor' component that allows users to manually adjust the color of individual stitches in the grid, providing a way to refine complex patterns generated by the AI.

src/utils/patternEditor.ts
src/components/ManualStitchEditor.tsx
src/App.tsx
src/components/StitchViewer.tsx
build
Built
# Create a 'Stitching Session Timer' feature that tracks how long a user spends on a pattern, displays it in the progress section, and calculates estimated remaining time based on their current stitching speed.

src/utils/timerStorage.ts
src/components/StitchSessionTimer.tsx
src/components/StitchProgressTracker.tsx
src/components/StitchViewer.tsx
src/App.tsx
build
Built
# Create a new 'Weekly Stitching Challenge' section that displays community-inspired pattern goals and allows users to set a specific daily stitch count target, showing a streak counter.

src/utils/challengeStorage.ts
src/components/WeeklyChallenge.tsx
src/components/Header.tsx
src/App.tsx
build
Built
# Add a feature to define custom project milestones (e.g., 'Finish Background', 'Complete Faces') linked to specific coordinate ranges, and display a progress bar for each milestone in the Stitch Progress Tracker.

src/components/MilestoneTracker.tsx
src/components/StitchProgressTracker.tsx
src/components/StitchViewer.tsx
src/App.tsx
build
Built
# Add a visualization component that displays a bar chart comparing the required skeins per DMC color versus the actual amount currently in the user's thread stash, highlighting potential thread shortages.

src/components/ThreadShortageChart.tsx
src/components/MyThreadStash.tsx
src/components/FlossLegendTable.tsx
build
Built
# Create a 'Stitching Techniques' reference panel in the sidebar that provides diagrams and instructions for common cross-stitch techniques like French knots, backstitching, and fractional stitches based on the current pattern's complexity level.

src/components/StitchingTechniquesSidebar.tsx
src/App.tsx
build
Built
# Analyze the 'Stitch Progress & Completion' card and add a small chart using Recharts that displays a historical trend line of daily stitch counts over the past 30 days to help the user visualize their progress consistency.

src/components/DailyStitchTrendChart.tsx
src/App.tsx
build
Built
# Create an 'Annotation Layer' feature that allows users to add sticky notes, color-coded flags, or custom text markers to specific coordinates in the 'StitchViewer' component.
# Add an integrated Pomodoro-style timer to the stitch viewer so users can track their actual time spent per session, which can then be logged towards their daily streak.

src/utils/annotationStorage.ts
src/components/PomodoroTimerWidget.tsx
src/components/AnnotationModal.tsx
src/components/AnnotationManagerDrawer.tsx
src/components/StitchViewer.tsx
src/App.tsx
build
Built
# Implement a 'Smart Sort' feature in the Floss Legend table that allows users to reorder colors by frequency (most used to least used) or by DMC numeric sequence.

src/components/FlossLegendTable.tsx
build
Built
# Add a 'Daily Stitching Goal' input to the Stitch Progress Tracker card, allowing users to set a specific number of stitches per day, and update the existing chart to show a progress bar comparing actual stitches vs. this goal.

src/components/FlossLegendTable.tsx
src/components/DesignComparisonModal.tsx
src/components/SavedDesignsGallery.tsx
src/components/StitchViewer.tsx
src/components/DailyStitchTrendChart.tsx
src/components/StitchProgressTracker.tsx
src/App.tsx
build
Built
# Implement a visual preview component in the Fabric Calculator that dynamically updates to show a rendered fabric color (e.g., White, Oatmeal, Black) behind a faint grid, helping users visualize their thread colors on their chosen fabric.

src/components/FabricPreviewCanvas.tsx
src/components/FabricCalculator.tsx
src/App.tsx
build
Built
# Update the SavedDesignsGallery component to include a 'Share' button on each saved design card, allowing users to copy a direct link to their pattern or share a preview image of their wedding design.

src/components/ShareSavedDesignModal.tsx
src/components/SavedDesignsGallery.tsx
src/App.tsx
build
Built
# Implement a responsive 'pinch-to-zoom' and drag-to-pan feature for the StitchViewer component to make navigating large wedding-sized patterns easier on mobile devices.
    
src/components/StitchViewer.tsx
build
Built
# Update the StitchViewer to include a 'Contrast Toggle' feature that displays the pattern in high-contrast mode (b&w) for better visibility during low-light stitching sessions.

src/components/StitchViewer.tsx
build
Built
# Add a 'Focus Timer' feature to the StitchProgressTracker, allowing users to start/stop a timer and automatically log the elapsed time as stitched progress.

src/components/StitchProgressTracker.tsx
src/App.tsx
src/components/StitchViewer.tsx
build
Built
# Update the StitchProgressTracker to allow users to define custom percentage-based milestones (e.g., '25% Complete', 'Wedding Day Ready') that trigger a celebration animation when reached.

src/components/PercentageMilestoneCelebration.tsx
src/components/StitchProgressTracker.tsx
build
Built
# Add a feature that allows users to export an animated GIF or a collage of their saved 'Progress Snapshots' to visualize their pattern growth over time.

src/utils/gifEncoder.ts
src/components/SnapshotExportModal.tsx
src/components/StitchViewer.tsx
build
Built
# Add a 'Reveal Mode' toggle to the StitchViewer that gradually uncovers the pattern grid based on the user's progress percentage, creating a 'scratch-off' effect for completed sections.

src/components/StitchViewer.tsx
build
Built
# Implement a 'Smart Noise Reduction' feature in the generator that automatically identifies and replaces isolated single-stitch 'confetti' colors with surrounding dominant colors, controlled by a slider in the PatternConfigurator.
    
src/utils/colorMatcher.ts
src/components/PatternConfigurator.tsx
# Add a numeric threshold input to the PatternConfigurator to define the 'confetti' sensitivity (e.g., how many adjacent stitches must be different for a color to be considered noise and auto-replaced).

src/utils/colorMatcher.ts
src/components/PatternConfigurator.tsx
src/App.tsx
build
Built
# Add a feature that allows users to add custom text annotations or labels directly onto the stitch grid, which will be saved with the pattern and appear in the exported PDF chart.

src/utils/annotationStorage.ts
src/components/AnnotationModal.tsx
src/components/AnnotationManagerDrawer.tsx
src/components/StitchViewer.tsx
src/components/SavedDesignsGallery.tsx
src/utils/pdfGenerator.ts
src/App.tsx
src/components/PrintPreviewModal.tsx
build
Built
# Implement an algorithm to automatically identify outline-heavy areas in the image to suggest 'backstitch' paths for the user to add manually in the ManualStitchEditor.

src/utils/outlineDetector.ts
src/utils/patternEditor.ts
src/components/ManualStitchEditor.tsx
# Create an 'Add Backstitch Outline' feature that allows users to select grid lines or objects in the pattern to add a decorative backstitch outline, generating a corresponding 'Backstitch Guide' page for the final PDF.

src/utils/outlineDetector.ts
src/components/BackstitchOutlineDrawer.tsx
src/utils/pdfGenerator.ts
src/components/PrintPreviewModal.tsx
src/components/StitchViewer.tsx
src/components/SavedDesignsGallery.tsx
src/App.tsx
src/components/ManualStitchEditor.tsx
build
Built
# Implement an automatic alert system in the MyThreadStash section that warns the user if their current stash is missing specific DMC codes required for the active pattern and provides a 'Copy missing codes' list for shopping.

src/components/MyThreadStash.tsx
src/components/FlossLegendTable.tsx
build
Built
# Create a 'Stitch Simulation' toggle that overlays a realistic thread texture on the grid pixels in the StitchViewer to help users visualize the finished embroidery look.

src/components/StitchViewer.tsx
build
Built
# Enhance the StitchViewer component to support keyboard shortcuts for grid navigation (arrow keys) and toggling stitch marks (Spacebar), making the experience more efficient for power users.

src/components/StitchViewer.tsx
build
Built
# Add a feature to export the current stitching progress data (stitchedCells) as a JSON or CSV file to allow users to back up their work or import it on a different device.
    
src/components/ProgressBackupModal.tsx
src/App.tsx
src/components/StitchViewer.tsx
src/components/StitchProgressTracker.tsx
build
Built
# Enhance the StitchViewer component to include zoom in and zoom out functionality (buttons and mouse-wheel support) to allow users to inspect fine details in larger pattern grids.
    
src/components/StitchViewer.tsx
build
Built
# Add a 'My Stash' toggle in the FlossLegendTable so users can mark which DMC colors they already own, and show a 'Missing Threads' view to help them shop for the remaining colors.

src/components/FlossLegendTable.tsx
build
Built
# Implement an 'undo' and 'redo' history stack for the stitch marking actions, allowing users to easily revert accidental clicks in the StitchViewer.

if __name__ == "__main__":
  pass  #
st.write("---")
st.caption("App setup completed.")
