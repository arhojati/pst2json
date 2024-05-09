convert pst to mbox file

```bash
# Install libpst
sudo apt-get install libpst4

# Convert PST to MBOX
readpst -r -o output_directory -M input.pst
```