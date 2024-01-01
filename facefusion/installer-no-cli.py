import subprocess

# Default options
TORCH_WHEEL = 'default'
ONNXRUNTIME_NAME = 'onnxruntime'
ONNXRUNTIME_VERSION = '1.16.0'


def install():
	# Uninstall existing installations
	subprocess.call(['pip3', 'uninstall', 'torch', '-y'])
	subprocess.call(['pip3', 'uninstall', ONNXRUNTIME_NAME, '-y'])

	# Install default torch
	if TORCH_WHEEL == 'default':
		subprocess.call(['pip3', 'install', '-r', 'requirements.txt'])
	else:
		subprocess.call(['pip3', 'install', '-r', 'requirements.txt', '--extra-index-url',
						 f'https://download.pytorch.org/whl/{TORCH_WHEEL}'])

	# Install default ONNX Runtime
	subprocess.call(['pip3', 'install', f'{ONNXRUNTIME_NAME}=={ONNXRUNTIME_VERSION}'])


if __name__ == "__main__":
	install()
