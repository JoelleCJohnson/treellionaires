import csv
import sys

def convert_spaces_to_commas(input_file, output_file):
    try:
        with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
            for line in infile:
                # Replace spaces with commas, but keep leading/trailing spaces
                processed_line = ','.join(line.split())
                
                # Restore newline character
                processed_line += '\n'
                
                outfile.write(processed_line)
        
        print(f"Conversion complete. Output written to {output_file}")
    except IOError as e:
        print(f"An error occurred while processing the file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    
    input_file = 'US.txt'
    output_file = 'USZips.csv'
    
    convert_spaces_to_commas(input_file, output_file)
