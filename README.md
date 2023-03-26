English | [简体中文](README_ch.md)
# AffectNet Dataset Preprocessing Tool
This Python tool can help you organize the uncompressed AffectNet dataset into a structure that can be directly read by Pytorch's ImageFolder method. This tool can help you start using the AffectNet dataset for deep learning research more quickly.

## How to Use

- Download and uncompress the AffectNet dataset(For most research, you only need to decompress the image compressed file ``Manually_Annotated.partX.rar`` in the ``Manually_Annotated`` folder and the corresponding label file ``Manually_Annotated_file_lists.zip``).
- Place this tool in the root directory of the AffectNet dataset.
- Run the ``affectnet_preprocess.py`` file as 
```shell
python affectnet_preprocess.py
```
- Or you can run the one-click processing script ``process.sh`` as:
```shell
bash process.sh
```
It will generate a folder ``AffectNet_class`` to store the processed dataset.

## Notes

- Before running this tool, make sure you have uncompressed the AffectNet dataset.
- After processing, there should be ``train`` and ``test`` folders under the dataset folder, and the eight expressions in it are stored in folders ``0-7``.
- We also provide file structure reconstruction scripts ``reconstruction.sh`` in case an error occurs during processing and needs to be restarted. run with the following code：
```shell
bash reconstruction.sh
```

## Contact Us

If you have any questions or issues while using this tool, please contact us.

## Support the Author

If this tool is helpful to you, you may consider buying me a cup of coffee. This is not mandatory, but your support will motivate me to contribute more to the community. Please note that supporting the author or not will not affect your discussion with me on this project or other related technologies. Thank you for your support!

![WeChat Pay](./pic/wechat_pay.jpg)
![Alipay](./pic/alipay.jpg)
