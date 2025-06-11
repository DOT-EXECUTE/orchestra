from pathlib import Path
import shutil

def copyTemplate(template_name: str, project_name: str) -> str:
    """Copies a template file to ../{project_name}/"""
    src = Path(__file__).parent.parent / "templates" / template_name
    
    # Destination path (new file to create)
    destDir = Path(f"{project_name}")
    destFile = destDir / template_name
    
    # Create destination directory if needed
    destDir.mkdir(parents=True, exist_ok=True)
    
    # Read template and write to new file
    with open(src, 'r') as src, open(destFile, 'w') as dest:
        dest.write(src.read())

    return str(destFile.resolve())
