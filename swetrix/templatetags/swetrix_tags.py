"""

MIT License

Copyright (c) 2022 Swetrix

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


script_element = 'https://swetrix.org/swetrix.js'
_img_element = f'https://api.swetrix.com/log/noscript?pid'  # TODO придумать как передавать проджект айди

swetrix_async_load_data = f'<script src="{script_element}" defer></script>'
swetrix_js_track = r"document.addEventListener('DOMContentLoaded', function () \{ swetrix.init("{YOUR_PROJECT_ID}"); swetrix.trackViews() \})"
swetrix_noscript_track = f'<noscript><img src="{_img_element}={YOUR_PROJECT_ID}" alt="" referrerpolicy="no-referrer-when-downgrade" /></noscript>'


register.simple_tag(
    func=lambda *args, **kwargs: mark_safe(
        swetrix_async_load_data,
        name='swetrix_async_load')
)

register.simple_tag(
    func=lambda *args, **kwargs: mark_safe(
        swetrix_swetrix_js_track.format(YOUR_PROJECT_ID=YOUR_PROJECT_ID),
        name='swetrix_js_track')
)

register.simple_tag(
    func=lambda *args, **kwargs: mark_safe(
        swetrix_noscript_track,
        name='swetrix_noscript_track')
    )

