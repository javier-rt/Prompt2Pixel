import streamlit as st
import models
import io

st.set_page_config(page_title="Impostor-AI", layout="wide", page_icon="🎭")

@st.cache_resource
def get_engine():
    """
    Initialize and cache the AI image generation engine.

    This function uses Streamlit's cache_resource to ensure the ImageEngine
    is only instantiated once, preserving memory and maintaining a single
    connection to the Hugging Face Inference API across sessions.

    Returns
    -------
    models.ImageEngine
        An instance of the ImageEngine class configured with the
        default SDXL model.
    """
    return models.ImageEngine()

img_engine = get_engine()

if "generated_image" not in st.session_state:
    st.session_state.generated_image = None


st.title("Prompt2Pixel")
st.subheader("Architecting Latent Diffusion Text-to-Image Synthesis on Serverless Infrastructure")

with st.container(border=True):
    col_input, col_output = st.columns([1, 1])

    with col_input:
        st.markdown("### Input Text")

        user_text = st.text_area(
            "Generate an image from text",
            placeholder="Describe the scene...",
            help="E.g.: A photo of me as a Viking king in a snowy forest.",
            key="user_text"
        )

        generate_btn = st.button("Generate Image", type="primary", use_container_width=True)

    with col_output:
        st.markdown("### Result")
        
        if generate_btn:
            if not user_text:
                st.warning("Please enter a text prompt.")
            else:
                with st.status("Processing AI Model...", expanded=True) as status:
                    try:
                        st.write("Synthesizing latent space...")

                        # Model call
                        response = img_engine.generate(user_text)
                        
                        st.session_state.generated_image = response
                        status.update(label="Generation completed!", state="complete", expanded=False)

                        buf = io.BytesIO()
                        st.session_state.generated_image.save(buf, format="PNG")
                        byte_im = buf.getvalue()

                        st.download_button(
                            label="Download Image",
                            data=byte_im,
                            file_name="impostor_ai_result.png",
                            mime="image/png",
                            use_container_width=True
                        )

                    except Exception as e:
                        st.error(f"Inference Error: {e}")
                        status.update(label="❌ Failed", state="error")
        
        # Show response
        if st.session_state.generated_image:
            st.image(st.session_state.generated_image, use_container_width=True)
        else:
            st.info("The generated image will appear here.")