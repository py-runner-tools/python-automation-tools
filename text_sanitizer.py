# ==========================================
# SCRIPT NAME: Text Sanitizer Utility
# PURPOSE: Automatically cleans and normalizes raw text strings
# ==========================================

def clean_text_data(raw_text):
    """
    Removes extra whitespaces, tabs, and line breaks from raw text inputs.
    Returns a clean, standardized single-spaced string.
    """
    cleaned_text = " ".join(raw_text.split())
    return cleaned_text

# Example execution test
if __name__ == "__main__":
    sample_input = "   Hello    world,   this is   a   messy   string.   "
    
    print("--- RUNNING TEXT SANITIZER ---")
    print("Raw Input    :", sample_input)
    print("Clean Output :", clean_text_data(sample_input))
  
