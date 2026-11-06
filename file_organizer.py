# ==========================================
# SCRIPT NAME: File Organizer Utility
# PURPOSE: Automatically sorts files in a directory into categorized folders
# ==========================================

import os
import shutil

def organize_files_by_extension(target_directory):
    """
    Scans a target directory and moves files into subfolders 
    based on their file extensions (e.g., Images, Documents, Scripts).
    """
    if not os.path.exists(target_directory):
        print(f"Error: Directory '{target_directory}' does not exist.")
        return

    # Dictionary of categories and their extensions
    extensions_map = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".csv", ".xlsx"],
        "Scripts": [".py", ".js", ".sh"]
    }

    print(f"--- STARTING ORGANIZATION: {target_directory} ---")
    
    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)
        
        # Skip directories, only process files
        if os.path.isdir(file_path):
            continue
            
        file_ext = os.path.splitext(filename)[1].lower()
        moved = False
        
        for category, extensions in extensions_map.items():
            if file_ext in extensions:
                category_dir = os.path.join(target_directory, category)
                os.makedirs(category_dir, exist_ok=True)
                
                shutil.move(file_path, os.path.join(category_dir, filename))
                print(f"Moved: {filename} -> {category}/")
                moved = True
                break
                
        if not moved:
            print(f"Skipped (Unknown extension): {filename}")

if __name__ == "__main__":
    # Example test path (Change this to your target folder path when running)
    print("File Organizer script loaded successfully. Ready for execution.")
