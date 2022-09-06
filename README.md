# autel-processing
Scripts used when processing surveys from Autel Evo II RPAS (https://shop.autelrobotics.com/collections/evo-ii/products/dual-640t)

When using imagery captured by the Autel Evo II Dual, the thermal TIFF files have insufficent contrast to align photos correctly. Starting data is stored as 32bit integers in a range representing only a couple percent of potential values.
IRX-processing.py is used to convert the data to uint16 and streach the data across possible values to increase apperant contrast for structure from motion software such as Agisoft Metashape Pro (https://www.agisoft.com/).

Currently the leading theory is that the values inside of the TIFF file represent the temperature in Kelven multiplied by 10 to remove need for decimals, though this still needs to be confirmed. The mathmatical transformation applied by this script takes the original image and subtracts 2722 making the numbers represent Celcius times 10. The data is then multiplied by 256 to streach to fill more of the uint16.

After photogrametic processing to convert output to temperature use a raster calculator to divide values in the orthomosaic by 2560 converting the values back to celsius.
