"""
Script kiểm tra hệ thống trước khi chạy ứng dụng
"""

import sys
import os

def print_section(title):
    print("\n" + "="*50)
    print(f"  {title}")
    print("="*50)

def check_python():
    print_section("PYTHON VERSION")
    print(f"Python: {sys.version}")
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print("✅ Python version OK (>= 3.8)")
        return True
    else:
        print("❌ Python version too old. Need >= 3.8")
        return False

def check_packages():
    print_section("CHECKING PACKAGES")
    packages = [
        "torch",
        "diffusers", 
        "transformers",
        "streamlit",
        "PIL",
        "accelerate",
        "safetensors"
    ]
    
    all_ok = True
    for package in packages:
        try:
            if package == "PIL":
                __import__("PIL")
            else:
                __import__(package)
            print(f"✅ {package:15s} - Installed")
        except ImportError:
            print(f"❌ {package:15s} - NOT FOUND")
            all_ok = False
    
    return all_ok

def check_cuda():
    print_section("CUDA & GPU CHECK")
    try:
        import torch
        
        print(f"PyTorch version: {torch.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")
        
        if torch.cuda.is_available():
            print(f"✅ CUDA is available!")
            print(f"   CUDA version: {torch.version.cuda}")
            print(f"   GPU count: {torch.cuda.device_count()}")
            print(f"   GPU name: {torch.cuda.get_device_name(0)}")
            
            # Test CUDA
            try:
                x = torch.rand(5, 3).cuda()
                print(f"✅ CUDA test successful")
                return True
            except Exception as e:
                print(f"⚠️  CUDA test failed: {e}")
                return False
        else:
            print("⚠️  CUDA not available - Will use CPU (slow)")
            print("   To enable GPU:")
            print("   1. Install CUDA Toolkit from nvidia.com")
            print("   2. Reinstall PyTorch with CUDA support")
            return False
            
    except ImportError:
        print("❌ PyTorch not installed")
        return False

def check_model_files():
    print_section("MODEL FILES CHECK")
    
    lora_path = "models/Kurzgesagt_v1.safetensors"
    
    if os.path.exists(lora_path):
        size_mb = os.path.getsize(lora_path) / (1024*1024)
        print(f"✅ LoRA model found: {lora_path}")
        print(f"   Size: {size_mb:.2f} MB")
        return True
    else:
        print(f"❌ LoRA model NOT FOUND at: {lora_path}")
        print("   Please ensure the model file is in the correct location")
        return False

def check_directories():
    print_section("DIRECTORIES CHECK")
    
    dirs = ["models", "outputs"]
    all_ok = True
    
    for dir_name in dirs:
        if os.path.exists(dir_name):
            print(f"✅ {dir_name:10s} - Exists")
        else:
            print(f"⚠️  {dir_name:10s} - Creating...")
            try:
                os.makedirs(dir_name)
                print(f"   Created successfully")
            except Exception as e:
                print(f"❌ Failed to create: {e}")
                all_ok = False
    
    return all_ok

def estimate_performance():
    print_section("PERFORMANCE ESTIMATE")
    
    try:
        import torch
        
        if torch.cuda.is_available():
            gpu_name = torch.cuda.get_device_name(0).lower()
            
            # Estimate based on GPU
            if "2050" in gpu_name or "4gb" in gpu_name:
                print("GPU: RTX 2050 or similar (4GB)")
                print("Expected performance:")
                print("  • 512x512, 50 steps: ~40-50 seconds")
                print("  • 640x640, 50 steps: ~60-70 seconds")
                print("  • Max safe resolution: 768x768")
            elif "3060" in gpu_name:
                print("GPU: RTX 3060 or similar")
                print("Expected performance:")
                print("  • 512x512, 50 steps: ~20-30 seconds")
                print("  • 768x768, 50 steps: ~40-50 seconds")
            else:
                print(f"GPU: {torch.cuda.get_device_name(0)}")
                print("Performance will vary based on GPU specs")
        else:
            print("⚠️  CPU mode - Will be VERY SLOW")
            print("Expected: 5-10 minutes per image")
            
    except:
        pass

def main():
    print("\n")
    print("🎨 Kurzgesagt AI Generator - System Check")
    print("=" * 50)
    
    results = {
        "Python": check_python(),
        "Packages": check_packages(),
        "CUDA/GPU": check_cuda(),
        "Model Files": check_model_files(),
        "Directories": check_directories()
    }
    
    estimate_performance()
    
    # Summary
    print_section("SUMMARY")
    
    for name, status in results.items():
        status_icon = "✅" if status else "❌"
        print(f"{status_icon} {name}")
    
    all_ok = all(results.values())
    
    print("\n")
    if all_ok:
        print("🎉 System check PASSED! You're ready to go!")
        print("   Run: streamlit run app.py")
    else:
        print("⚠️  Some issues found. Please fix them before running.")
        print("   See details above.")
    
    print("\n")

if __name__ == "__main__":
    main()
