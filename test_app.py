import streamlit as st

st.title("Test App")

# Test imports từng cái
try:
    import torch
    st.success(f"✅ torch {torch.__version__}")
    st.info(f"CUDA: {torch.cuda.is_available()}")
except Exception as e:
    st.error(f"❌ torch: {e}")

try:
    import diffusers
    st.success(f"✅ diffusers {diffusers.__version__}")
except Exception as e:
    st.error(f"❌ diffusers: {e}")

try:
    from diffusers.pipelines import StableDiffusionPipeline
    st.success("✅ StableDiffusionPipeline imported")
except Exception as e:
    st.error(f"❌ StableDiffusionPipeline: {e}")

st.write("All tests done!")
