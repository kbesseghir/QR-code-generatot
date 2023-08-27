from django.shortcuts import render
import qrcode
from io import BytesIO
import base64

def generate_qr_code(request):
  qr_image_base64 = None

  if request.method == 'POST':
    url = request.POST.get('url')

    if url: 
        qr_image = qrcode.make(url)
        qr_image_stream = BytesIO()
        qr_image.save(qr_image_stream)
        qr_image_stream.seek(0)
        qr_image_base64 = base64.b64encode(qr_image_stream.read()).decode('utf-8')
        

    return render(request, 'index.html', {'qr_image': qr_image_base64,'url':url})

