import os

# Path to the directory containing .mp3 files
directory_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data_modao')

for filename in os.listdir(directory_path):
    if filename.endswith('.mp3') or filename.endswith('.wav'):
        # Create a corresponding .txt file name
        txt_filename = os.path.splitext(filename)[0] + '.txt'
        txt_filepath = os.path.join(directory_path, txt_filename)
        
        if not os.path.exists(txt_filepath):
            with open(txt_filepath, 'w') as txt_file:
                txt_file.write('')

        print(f'Created: {filename} -> {txt_filename}')

print('All .txt files have been created.')
