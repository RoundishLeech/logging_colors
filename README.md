# logging_colors.py

Updated logging_colors.py used by text-generation-webui to address following error:

Traceback (most recent call last):
  File "D:\text-generation-webui-main\modules\ui_model_menu.py", line 198, in load_model_wrapper
    shared.model, shared.tokenizer = load_model(shared.model_name, loader)
  File "D:\text-generation-webui-main\modules\models.py", line 86, in load_model
    tokenizer = load_tokenizer(model_name, model)
  File "D:\text-generation-webui-main\modules\models.py", line 105, in load_tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
  File "D:\text-generation-webui-main\installer_files\env\lib\site-packages\transformers\models\auto\tokenization_auto.py", line 736, in from_pretrained
    return tokenizer_class.from_pretrained(pretrained_model_name_or_path, *inputs, **kwargs)
  File "D:\text-generation-webui-main\installer_files\env\lib\site-packages\transformers\tokenization_utils_base.py", line 1854, in from_pretrained
    return cls._from_pretrained(
  File "D:\text-generation-webui-main\installer_files\env\lib\site-packages\transformers\tokenization_utils_base.py", line 2017, in _from_pretrained
    tokenizer = cls(*init_inputs, **init_kwargs)
  File "D:\text-generation-webui-main\installer_files\env\lib\site-packages\transformers\models\llama\tokenization_llama.py", line 141, in __init__
    logger.warning_once(
  File "D:\text-generation-webui-main\installer_files\env\lib\site-packages\transformers\utils\logging.py", line 305, in warning_once
    self.warning(*args, **kwargs)
  File "D:\text-generation-webui-main\installer_files\env\lib\logging\__init__.py", line 1489, in warning
    self._log(WARNING, msg, args, **kwargs)
  File "D:\text-generation-webui-main\installer_files\env\lib\logging\__init__.py", line 1624, in _log
    self.handle(record)
  File "D:\text-generation-webui-main\installer_files\env\lib\logging\__init__.py", line 1634, in handle
    self.callHandlers(record)
  File "D:\text-generation-webui-main\installer_files\env\lib\logging\__init__.py", line 1704, in callHandlers
    lastResort.handle(record)
  File "D:\text-generation-webui-main\installer_files\env\lib\logging\__init__.py", line 968, in handle
    self.emit(record)
  File "D:\text-generation-webui-main\modules\logging_colors.py", line 39, in new
    args[0]._set_color(color)
AttributeError: '_StderrHandler' object has no attribute '_set_color'

It seems that the error is occurring because the _StderrHandler class is being used instead of the custom CustomStreamHandler class. The _StderrHandler class is part of the logging module and does not have the _set_color method.
