# sd_forge_hypertile_svd_z123
将 [forge-legacy-extensions](https://github.com/lllyasviel/forge-legacy-extensions) 中的插件移植到 [stable-diffusion-webui-forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) / [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)。


## 安装
### 通过命令安装

进入 stable-diffusion-webui-forge / stable-diffusion-webui 的 extensions 目录。

```bash
cd extensions
```

使用 Git 命令下载该扩展。

```bash
git clone https://github.com/licyk/sd_forge_hypertile_svd_z123
```


### 通过 stable-diffusion-webui-forge / stable-diffusion-webui 安装
进入 stable-diffusion-webui-forge / stable-diffusion-webui 界面后，点击`扩展`->`从网址安装`，将下方的链接填入`扩展的 git 仓库网址`输入框。

```
https://github.com/licyk/sd_forge_hypertile_svd_z123
```

点击`安装`下载该扩展。


## 模型下载

### Stable Video Diffusion
从此处下载 Stable Video Diffusion 模型。

- [svd.safetensors](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid/blob/main/svd.safetensors)
- [svd_xt.safetensors](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/blob/main/svd_xt.safetensors)

下载后将模型放在以下目录。

- [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)：`stable-diffusion-webui/models/svd`
- [stable-diffusion-webui-forge](https://github.com/lllyasviel/stable-diffusion-webui-forge)：`stable-diffusion-webui-forge/models/svd`。


### Stable Zero123
从此处下载 Stable Zero123 模型。

- [stable_zero123.ckpt](https://huggingface.co/stabilityai/stable-zero123/blob/main/stable_zero123.ckpt)

下载后将模型放在以下目录。

- [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)：`stable-diffusion-webui/models/z123`
- [stable-diffusion-webui-forge](https://github.com/lllyasviel/stable-diffusion-webui-forge)：`stable-diffusion-webui-forge/models/z123`。
