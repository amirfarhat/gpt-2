# first, download the shakespeare dataset
python download_dataset.py

# then download the relevant model sizes
python download_model.py 124M &
python download_model.py 355M &
python download_model.py 774M &
wait
