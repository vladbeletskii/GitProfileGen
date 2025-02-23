import json

def load_config():
    with open("config.json", "r", encoding="utf-8") as file:
        return json.load(file)

def load_template():
    with open("template.md", "r", encoding="utf-8") as file:
        return file.read()

def generate_readme():
    config = load_config()
    template = load_template()
    
    # Подставляем данные
    readme_content = template.format(**config)
    
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(readme_content)
    
    print("✅ README.md успешно создан!")

if __name__ == "__main__":
    generate_readme()
