import pymem
import re

pm = pymem.Pymem('csgo.exe')
csgo = pymem.process.module_from_name(pm.process_handle,
                                        'csgo.exe')

csgoModule = pm.read_bytes(csgo.lpBaseOfDll, csgo.SizeOfImage)
address = csgo.lpBaseOfDll + re.search(rb'.\x1A\xF6\x45\x0C\x20',
                                         csgoModule).start()

pm.write_uchar(address, 0xEB if pm.read_uchar(address) == 0x74 else 0x74)
pm.close_process()
