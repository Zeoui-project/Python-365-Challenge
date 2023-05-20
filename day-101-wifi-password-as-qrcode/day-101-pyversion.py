# %% [markdown]
# # Wifi Password as QR Code using Python

# %%
%pip install wifi_qrcode_generator

# %%
import wifi_qrcode_generator
qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
    ssid='Home WiFi', hidden=False, authentication_type='WPA', password='very complicated password'
)
qr_code.print_ascii()
qr_code.make_image().save('qr.png')