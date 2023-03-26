[English](README.md) | 简体中文
# AffectNet数据集预处理工具
这个Python工具可以帮助您将解压后的``AffectNet``数据集整理成可以直接被Pytorch中``ImageFolder``方法读取的结构。这个工具可以帮助您更快地开始使用``AffectNet``数据集进行深度学习研究。

## 使用方法

- 下载并解压缩AffectNet数据集（对于大多数研究，您只需要解压缩``Manually_Annotated``文件夹中的图像压缩文件``Manually_Annotated.partX.rar``和相应的标签文件``Manually_Annotated_file_lists.zip``）。
- 将此工具放置在``AffectNet``数据集的根目录中。
- 运行如下代码：
```shell
python affectnet_preprocess.py
```
- 或者你可以使用一键脚本如下：
```shell
bash process.sh
```
它将生成一个名为``AffectNet_class``的文件夹，用于存储处理后的数据集。

## 备注

- 在运行这个工具前，确保你已经按要求解压了数据集和标注。
- 在处理结束后，数据集文件夹下应该有``train``和``test``文件夹，其中包含了8种表情，存储在``0-7``文件夹中。
- 如果处理过程出现错误并需要重新启动，请使用文件结构重建脚本``reconstruction.sh``，使用以下代码运行：
```shell
bash reconstruction.sh
```

## 联系我

如果您在使用此工具时有任何问题或疑问，请不要犹豫联系我。

## 支持作者

如果这个工具对你有帮助，你可以选择给我点一杯卡布奇诺。但这不是强制的，并且无论是否赞助都不会影响与我就此项目或其他相关技术的讨论。谢谢你的支持！

<div align="center">
    <img src="./pic/wechat_pay.jpg" width="40%" alt="微信支付">
    <img src="./pic/alipay1.jpg" width="40%" alt="支付宝">
</div>
