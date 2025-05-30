 Copyright (c) 2025 devgagan : [https://github.com/devgaganin](https://github.com/devgaganin). 
# Licensed under the GNU General Public License v3.0. 
# See LICENSE file in the repository root for full license text.

from pyrogram import filters
from pyrogram.types import Message # Message tipini içe aktarıyoruz, kodun daha anlaşılır olması için

user_steps = {}

# login_filter_func fonksiyonunu güncelliyoruz
# Bu fonksiyon, gelen 'message' objesinin bir 'from_user' özelliğine sahip olup olmadığını kontrol eder.
# Eğer 'from_user' yoksa (yani None ise), 'id' özelliğine erişmeye çalışmak hataya neden olur.
# Bu yüzden, 'from_user'ın varlığını kontrol ediyoruz.
def login_filter_func(_, __, message: Message):
    # message.from_user'ın None olup olmadığını kontrol et
    if message.from_user:
        # Eğer from_user varsa, id'sine güvenle erişebiliriz
        user_id = message.from_user.id
        # user_id'nin user_steps sözlüğünde olup olmadığını kontrol et
        return user_id in user_steps
    else:
        # Eğer from_user yoksa (örneğin, bir kanal gönderisi veya servis mesajı),
        # bu filtre bu durumu işlemesin ve False döndürsün.
        return False

# Filtreyi oluştur
login_in_progress = filters.create(login_filter_func)

# Kullanıcının adımını ayarlayan fonksiyon
def set_user_step(user_id, step=None):
    if step:
        user_steps[user_id] = step
    else:
        # Eğer adım belirtilmezse, kullanıcıyı user_steps'ten çıkar
        user_steps.pop(user_id, None)

# Kullanıcının mevcut adımını getiren fonksiyon
def get_user_step(user_id):
    return user_steps.get(user_id)
