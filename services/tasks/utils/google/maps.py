import json
import re

import requests
import time
from multiprocessing.pool import Pool
from typing import List
from google.config import MAP_KEYWORDS, FILTERABLE_TAGS
from google.proxy import Proxy
from timezone_functions import create_hour_dict



def scratch(tfid):
    lat = '29.424349'  # San Antonio
    long = '-98.491142'
    Maps().get_place_details(tfid, lat, long)


def test():
    lat = '29.424349'  # San Antonio
    long = '-98.491142'
    #
    # long = '-77.050636'  # DC
    # lat = '38.889248'
#     tfids = [
#     "0x865c5dfc7c505721:0xccefea44b78f8fa0",
#     "0x865c5cb8e580594b:0xbffcd6cfad0744d0",
#     "0x865cf4a54c9ae781:0x8da73d5e005bd68",
#     "0x865c8a80ade98cfb:0x8b74e26b95066998",
#     "0x865c595b1870ac23:0x44eb987777fc00f",
#     "0x865c58ab1eed0463:0x7c9c87ddf9d48f10",
#     "0x865c5f61e0adb147:0xf6883a77ced09faa",
#     "0x865c5f70ef6ebbbb:0xa201376dcb2cb88f",
#     "0x865c8a586f8500b3:0xfc67116b2978b20a",
#     "0x865c8d6d56dcea01:0x7d50436745724840",
#     "0x865c5f8675140869:0x159f0b0ebb85682a",
#     "0x865c6766d8d7037b:0xbb5caed11dcd65e4",
#     "0x865c5c69f25ac68b:0xaeafabe599e8e2c5",
#     "0x872b4378a37942d3:0x7cfb6eb61e93c2d5",
#     "0x865cf63ca605ddaf:0x971de95d5ffdb72e",
#     "0x865c58bb4af92c95:0x118a1d388c80de7b",
#     "0x865c92e1958641f7:0xedc9eb4236834852",
#     "0x865c5e1a8e46a943:0xfe13645303676550",
#     "0x865cb81f2bfbb2d1:0x3edcac0a835a9ace",
#     "0x865c4f344475142d:0x552099dd6bb28d98",
#     "0x865c682be902fae7:0x220727b5ff6f18d4",
#     "0x865c5f21b79b671b:0x40bebaa62ffc968",
#     "0x865c5f54c38edb27:0xab8df345c6ae392a",
#     "0x865cf5f3e08ee881:0x40f0a4128222e5bd",
#     "0x865cf5f05a599cf3:0xf3dc652d93ec17d4",
#     "0x865c58ab087f8dfd:0x55616d27d8d37351",
#     "0x865c5baa2d15a86d:0x756fa57b58e37805",
#     "0x865cf7039d9f7abf:0xc23c5c7366395d88",
#     "0x865c432fbb121d59:0x6bcb183227d120a8",
#     "0x865c5f53528991f9:0xcdba7605d3c5854f",
#     "0x865c60fd979788c3:0x5a3822d41895b2bc",
#     "0x865c59b0efc1433b:0x3f8d5ee195c1fcc9",
#     "0x865c5c9f92c55555:0x96677f8f6f358d37",
#     "0x865cf597667bcf47:0x10e33edb7592941a",
#     "0x865cf4aa20436cef:0x47ca5c084fe32547",
#     "0x865cf770e1c4841f:0x7adeabb569970f28",
#     "0x865c600cbfe06b05:0x6ab8623853b7ca65",
#     "0x865c5e1079c48bd3:0xf80dd3583bf73525",
#     "0x865c5860d06de63d:0xd327c389973f71f9",
#     "0x865c60f646d92c3d:0xe8c70cf1b28e593",
#     "0x865c60b65853262b:0x1b2ac613e6efd895",
#     "0x865c58ad7894764b:0x20b2a42a19c4954e",
#     "0x865cf39e852f0695:0x658951dd00d5abf5",
#     "0x865c59b5a9085411:0xb6559b45c883c42",
#     "0x865c58ab4c536859:0x3f2dcea78d911378",
#     "0x865c600bad5bf59b:0x389852916b3cd269",
#     "0x865c8acb9bca8a33:0x4fd97acc90fa6d4c",
#     "0x865c58ab3523788b:0x697b58fedc700f73",
#     "0x865c59b4f4f15837:0x1f02a654b7600376",
#     "0x865c600b935f6995:0x4686e6ed5dc7a39b",
#     "0x865c59cb52bc7a83:0xe2dd39827d574d4f",
#     "0x865c5f2ebe377cf1:0x2bbf7f4d1c5d76e1",
#     "0x865c8c83c317940f:0xf314db71ce746676",
#     "0x865c8c951629beab:0x64e3966f7821bcac",
#     "0x865cf5f6842efb3f:0xc7003329abf3ddc0",
#     "0x865c5e10cdbae35b:0x4e78e74cc11ce022",
#     "0x865c5874a60b09e3:0x83261cfca8062c23",
#     "0x865c5f30a7543a3d:0xfc73e1d750300b9e",
#     "0x865cf7a6553fedaf:0x9ba0bc96ee06f698",
#     "0x865c8a874cca3959:0xd7b0c1ec2dbde154",
#     "0x865c5f549a055555:0x43aaf0b56eec744b",
#     "0x865cf454eb306853:0xcbf6469a131f1336",
#     "0x865c5f444a6d0535:0x8f3ef3471995f1de",
#     "0x865cc190a1d5da0f:0x7e543ddfad12416e",
#     "0x865c5d3449365ffb:0xaa84b6346c3de995",
#     "0x865cb618191bb1d5:0x12873a82279694a0",
#     "0x865c600b057d2905:0xe364a5e4f9327f2f",
#     "0x865c676f32ca4f6f:0xbfbed1b73b2a9b11",
#     "0x865c5c44f73ab295:0xc746866058ce114b",
#     "0x865c5f85ab4190a7:0x63050311d6c93f4f",
#     "0x865c8b1087eb7bcb:0xbb809fba6403b3a6",
#     "0x865c5d03bc2583fd:0x3c0603de9e88a4cb",
#     "0x865c24a1219a195d:0xe8cfd59ec0a1d5cd",
#     "0x865c5e8edcded4e7:0x3687bf0aea3e435b",
#     "0x865c5fa9173f1981:0x7f1d4ccdf2f7d8b",
#     "0x865c600ca8355cc9:0xce0734cebd1e72a8",
#     "0x865c5e6dbf69df5b:0x997e338131e377e5",
#     "0x865cf357d9dd528b:0xf5b71f14669a75d5",
#     "0x865cf5f69fc7a383:0x50058db99fe45734",
#     "0x865cf5e9e1ce9091:0x9a239f6a6b96820b",
#     "0x865c4383f698379b:0xf9705e63481d6f1e",
#     "0x865cf5f18d04574f:0x264e1707444663b0",
#     "0x865c5dbc5a1c7f77:0x134317b21c29f9e1",
#     "0x865cf5f6911669b3:0xd97498c2ada38cea",
#     "0x865c58ab66904389:0x1538dd738d18d6ff",
#     "0x865c678bedb102e9:0x4fdba33e09f4142b",
#     "0x865c5f54c22d1cc1:0xfd39489547dbff93",
#     "0x865cf293d20a361d:0xa864a1941a531853",
#     "0x865c5fee5f42866d:0xfe644febf7bc4ad",
#     "0x865c5d95da1783b1:0x3f311e78bbd45eac",
#     "0x865c672dfa28a423:0xc8d8dd7d64fddc14",
#     "0x865c5ce9e1c82aa5:0x4b4142b9a5812cba",
#     "0x865c5e21ea71e18f:0x6cc83c3403959bc",
#     "0x865cf73f2b9c3867:0x8db4a928f97bb147",
#     "0x865c66e6a7fc20af:0xc1ba02ffe516e594",
#     "0x865cf64a59ad4953:0xf57afb86614f59db",
#     "0x865c5f54c6727e9d:0xfe6a636d1eb4351b",
#     "0x865c5e1ae6789105:0xd0fba83a465c5b8f",
#     "0x865c58ab445deb49:0x8aa69dcb09196e37",
#     "0x865c5f440c53ebb3:0x8f1b97db0b2b7bd",
#     "0x865c676636902709:0xa3c7d90c320856f8",
#     "0x865c93be81a545b1:0xb6eec4af6966355d",
#     "0x865cf531807edd7f:0xec95f3a926bce639",
#     "0x865cf53376971385:0x6b4fec01b6899ff2",
#     "0x865c92a2dd75a74d:0xefe93a657ae4a677",
#     "0x865c58aa91580159:0x82fb468df5ffd0ca",
#     "0x865cf6055f106271:0xfc26c15d933f5790",
#     "0x865c66440f2804d3:0x887071738ad7ead4",
#     "0x865c58b26e352a9d:0x1906f85f142f901b",
#     "0x865cf606b372d921:0x3ec7045d9b0f546f",
#     "0x865c42e1b8294e8f:0x6baeff9034c8c95",
#     "0x865cf7de2563a793:0xf8517782e7747820",
#     "0x865cf3887a0eba1f:0xea78c95046208f14",
#     "0x865c5fb23c1d79a1:0xe8cadc7be486b6c",
#     "0x865cf599efb07d2f:0xef2d427e59dd57e6",
#     "0x865c8aeb5fb59a4b:0xf1398416fd041090",
#     "0x865c58bc2de29755:0xc227e71f3563d4f4",
#     "0x865c5f52884edaef:0x44e45afffd1e67ab",
#     "0x865cf5ff25a33fe5:0x41406fe0af794d09",
#     "0x865c6001d18786e5:0x3581f78365643e56",
#     "0x865c58ab606970e3:0x538ea1c724f9bd11",
#     "0x865cf60af78c46eb:0xe1eea9b2e6d26318",
#     "0x865cf7d348c653d7:0xdd4a857d7f8dc78d",
#     "0x865cf606ca4139c7:0x56251ba3ac739bbf",
#     "0x865c605f438f712f:0xc58eb951a777cd5c",
#     "0x865c600bb736c8cb:0x5585be98c265501a",
#     "0x865c5c970bdbba13:0x6f355fa361c91cde",
#     "0x865c5ecc6b81c1cf:0x86aabd695a1f428a",
#     "0x865cf602115118f7:0xa0b0f979ba051cd5",
#     "0x865cf5f6b843edc9:0x72461ee8693026f4",
#     "0x865c5daa0d23eab7:0x4d27371d24fe48bf",
#     "0x865c60f5fa69047d:0x91cb482c76325dda",
#     "0x865c8d7c48920293:0x4daa20e9770fde83",
#     "0x865c5ff569e54bf3:0xd999c39a20ee0347",
#     "0x865c58af4482f879:0x66877e906bcd8679",
#     "0x865c60375080433d:0x32feac3c691b71d1",
#     "0x865c5ffd7451766f:0x7a3f57970aff8ba1",
#     "0x865c43c0dc4dbb33:0xd9197e1dbf0cfd73",
#     "0x865cf560fb9e27ed:0x386b3f013a720968",
#     "0x865c8be423c59e17:0xcfe31bc8e5aadcba",
#     "0x865c61d4b7d2d90b:0xb8592c3b08d64a8b",
#     "0x865c5f52375c5385:0xa7c50b08ed72b0bc",
#     "0x865c58a926ce2469:0x5e22da6fe2444dfe",
#     "0x865c5fee9853cf27:0x39d28fd35d770bfe",
#     "0x865cb81953b18e6d:0xd7731542c9fdf1a3",
#     "0x865c5f6e936cb8d1:0xff775643d46e8364",
#     "0x865c581521860b47:0x6685da263d10884e",
#     "0x865c936ad81257e9:0x7eb43fb98850f97",
#     "0x865c8d75bf609f01:0x41bc36392072ccb1",
#     "0x865c601a3c619dd7:0xeb2a273bddf4d864",
#     "0x865cf5e78ae780e9:0x7619148d80c182d4",
#     "0x865cf59fc1af657b:0x615b947f4fa4b75b",
#     "0x865c6732104bfb2f:0x1cefa739cdc999ce",
#     "0x865c686944106921:0xe8d253565395a7e6",
#     "0x865c5f4c94217061:0x22dd26e7a9964b8e",
#     "0x865cf6044d4fffff:0xe2258344f86e907c",
#     "0x865cf4bf7bb4a4fb:0x7ecb21c381e6332c",
#     "0x865c58a93945ad09:0x872d0b1eda4c6771",
#     "0x865c5e5076c25eb1:0x863a456e5b8b7252",
#     "0x865c5d7d7b9582b1:0x6d99c28a9da2cb24",
#     "0x865c5b17fe44c38b:0xcd7541066cd1932d",
#     "0x865c58ab3011c6e9:0x1ba1d52ba5f959c5",
#     "0x865c58ab1c86a535:0x1f6b932f295cc673",
#     "0x865c61f86532dfd9:0x5465fcfd03abf86d",
#     "0x865c67ed348a0247:0xef7bd1e99f6bb8a2",
#     "0x865c5d49ed43bfdd:0x8bdc13e0b280e412",
#     "0x865c58aa9216c511:0x47dea3c0feee2b7a",
#     "0x865c591e84a62623:0xcb5fcdb252b94291",
#     "0x865c58ab1798b3bf:0xd3aebb4459eaf4ea",
#     "0x865c8a91e8ae2f67:0xcb5e25b8fdebe707",
#     "0x865c6006f6e0ae25:0x930b8bff8ad6faa1",
#     "0x865c5d00f79501ef:0x200fe3dc2fb0accf",
#     "0x865cf83d0034b911:0x7b44dca2731f4add",
#     "0x865c673221fa26cb:0xe531cf5fd2466998",
#     "0x865c8d6d71e85d63:0xf7ec7e22940971b5",
#     "0x865cb81cab95163f:0x6f66aea4a9cb449d",
#     "0x865c5f5f06f35503:0x35d7bf5bad50838e",
#     "0x865c5f5ca63f5ae9:0x937e48f1b63a7fe3",
#     "0x865c5e1a9d8efb8b:0x18f11a7acfdb53c6",
#     "0x865cf560fb9e27ed:0x4172beb576e5793",
#     "0x865c5feee661cd05:0x6ad715d59501acb9",
#     "0x865c5ffe77442f77:0x7cac731956456332",
#     "0x865cf52c44c724af:0x615ca529c6af63c9",
#     "0x865c59efe326875f:0x46a39147f2676a9c",
#     "0x865cf1552946ef7d:0xc8988b9a29b60103",
#     "0x865c5cb83af4f467:0x284184a4a730073b",
#     "0x865c593f24e2ad45:0x1b0190178485956b",
#     "0x865c8ab55fde58f9:0xcdd81acd03635f79",
#     "0x865c8b0b6c9c5c5b:0x3a210eb2ab17cfde",
#     "0x865c602a8290d7fb:0x20425e7e8092cce5",
#     "0x865c6175ea127753:0xbab1f391cf400330",
#     "0x865c5f5b5e357123:0x2dacb65a1bb569e",
#     "0x865c8d6f54d1e2fb:0xb3602ea5f879f3f7",
#     "0x865c5d035a059be9:0x3fda9bfe4b49f082",
#     "0x865cf674bb55e5e3:0x316e8646e8c7ed27",
#     "0x865c8d859525a065:0x85b5c474d3c9813a",
#     "0x865c5e9ac8b45679:0xf120b483d9cc978a",
#     "0x865cf5febc78856b:0x5ac399b6f88066e8",
#     "0x865c5f678d59d6f3:0xec17cb4153528d91",
#     "0x865cf6013440d52d:0xc5be1eb152411cfa",
#     "0x865c61d4d2cb1f69:0xe9b4f69210edc238",
#     "0x865c600b061bc481:0xdd98b19127e9f7f3",
#     "0x865c5f536b172aff:0x4fb483a05092e77c",
#     "0x865c43ea3dabf029:0x91b16581c124d424",
#     "0x865c5f56b48c0cad:0x64bc35667a997a41",
#     "0x865c5f54ba0b65ad:0xcc3d6ce143197623",
#     "0x865c5f54d83d0f4f:0x46ee2641cc4d93bb",
#     "0x865c589d2ea757a5:0xa239a45bdce049be",
#     "0x865c5eecf5b3ffff:0x84ccbe3185414df3",
#     "0x865c58d5bbb3946b:0xc071c8afae65a053",
#     "0x865c42e37ff51ddf:0x87d0ea67c43fae04",
#     "0x865c5d34119c9a97:0x2dcdd53fa66abf2a",
#     "0x865c5fb42eedc4ab:0x40150c21277cbbc4",
#     "0x865c58a8d907ac7f:0xc53df661116e19e4",
#     "0x865c5f6941c480f9:0x116e6389ed41881",
#     "0x865c58ac82bf1e4f:0x4f795f4f3651c722",
#     "0x865cf52d6c94d47f:0xac1efa9e308b498a",
#     "0x865c5f1515e919df:0xd2018654ad4bc9b0",
#     "0x865c58ab41b75669:0x15d55dc26302b744",
#     "0x865cf57b6e040951:0x8892b767ac7e0bd",
#     "0x865cf628e7500173:0x2452262c3c9488e6",
#     "0x865cf5736bc53883:0x569a58dd3cc1c8c4",
#     "0x865c58acce0f354b:0x5eaf40831ff79254",
#     "0x865c608142c8e12b:0xeedbeeaa5f4efd56",
#     "0x865c4354f496c9e7:0x59a096f4bc7d6156",
#     "0x865cf4fa37e536b3:0x5a8cc79bfca06724",
#     "0x865c5f69485106a7:0x4f2968e64e57cae2",
#     "0x865c58ab1804281f:0xd25731f16fedd5ea",
#     "0x865c59b4fdd2ba35:0xb009ff42d8f00629",
#     "0x865c5927aed64d39:0x81c825bc8e44fee7",
#     "0x865c59bc4544e3ff:0x117de4d33ff0b8ba",
#     "0x865c5dcc49d75ee7:0xa854d470c6018f83",
#     "0x865c5f60f4596773:0x2f7db587584d33dd",
#     "0x865c5b7a66422cd9:0x1490c1a4ef1f8239",
#     "0x865c5f8a8f94d093:0x6b74cb18986a051a",
#     "0x865c8b68ec4096cd:0x5bda7813920a95d3",
#     "0x865c5f676599ce2d:0x5272cf46053d3d9c",
#     "0x865c8ca71255327b:0x7e38378570e2fd0a",
#     "0x865c5f7a4a26ce95:0x2256c82f4e1c94e1",
#     "0x865c66d8b0c6d37b:0x729670492218a8b",
#     "0x865cf554c4bd0e8d:0x4331ca9cdc9bb8ab",
#     "0x865c58a8d88aeb0b:0xd8dec2331fe57c5",
#     "0x865c59d9d2662a69:0xa7b881d57b77a789",
#     "0x865cf7d029998c19:0xfdc1d4910d9d0d39",
#     "0x865c5f604cce19cb:0xf6a75bfcb79cb0ad",
#     "0x865cf773ead2cef5:0xb359e529cfd03988",
#     "0x865c60b27b722ccf:0x8f718f2016ab2e40",
#     "0x865c5862413f5b6d:0x66a4ca483184de9b",
#     "0x865cf58215486f65:0x8bc1f8a9f51ba885",
#     "0x865cf7ae6e038f75:0x561e0781d595d943",
#     "0x865c5b7097b74723:0x830c5f876ed37022",
#     "0x865c5d957dfdf87b:0xb4f31452c73840f6",
#     "0x865c93e7e87a33a1:0x16b969700751501b",
#     "0x865c58ab087f8dfd:0x4488c22918d877fa",
#     "0x865c437791fd4c2f:0x22ce37ba1f5dc49f",
#     "0x865cf98a67d0f1cd:0x64be85ec5c30f80e",
#     "0x865c600bcf072a7d:0x43f5796dbd8b996d",
#     "0x865c5e0a3b44b59b:0x1c5b74980ee6383f",
#     "0x865c600bc8e0a205:0xe50e65c4dfa64861",
#     "0x865cf4c09b61f601:0x3bc9802de4d79399",
#     "0x865cf555b53874b3:0xe477c9147f047b42",
#     "0x865c5f604d74c451:0x5cad610ee89e3c0f",
#     "0x865c8d6612ff7f1b:0x495d46444bc972b9",
#     "0x865c5f5ca73243c7:0xf7190f61d34dd3c",
#     "0x865c5f19f452fa8f:0x155670a8f0282cc4",
#     "0x865cf79df12b521d:0xa12b1343f1ba6be6",
#     "0x865c5ca7ee571009:0xb66eed4934b72e8",
#     "0x865c5d0155555555:0x1ff21889f8ffd4a1",
#     "0x865c679f81d8770f:0x342b7cfa6f58bd52",
#     "0x865c66cd2c15fc69:0xfc7b9b45d600c4d3",
#     "0x865cf69ea3cd6e2d:0xf81c1202f0b33979",
#     "0x865c5b64ebeac029:0x57da8c259fc0ab51",
#     "0x865c60ae71dc7603:0x437175a1e501505c",
#     "0x865c5e15fd4c4593:0xf866a3199db479f0",
#     "0x865c598c847b1d1d:0x6ac5c07f3db7e461",
#     "0x865c5f54fc901dbd:0x18ab61c396f3c252",
#     "0x865c670784dbc1f5:0x822fabaf70a9c227",
#     "0x865c92e34af9c325:0x88e1159fd848a2d0",
#     "0x865cf39f746afba9:0xcb2b45efc047064b",
#     "0x865c6624a353ea27:0xec2417a4664a482c",
#     "0x865c5ccaa1100fe9:0x74283db71673830d",
#     "0x865cf5491a63c21d:0x87b46f37278c8435",
#     "0x865c8a923e516313:0x9def4428ae2405dd",
#     "0x865c42631bd076af:0x800809baeed2f545",
#     "0x865c58aa8121136f:0x3a71e0ff3492c7ce",
#     "0x865cf59fe5e352ff:0x80c57ee09ed7a32c",
#     "0x865cf607733d4e57:0xf66e174da8992fff",
#     "0x865c5eaff393d5cb:0xe066eef92e5b5a39",
#     "0x865c8c8efa367b2d:0x92382cb1e2c9f0c2",
#     "0x865cf54165c4583f:0x92c760f5345b43af",
#     "0x865c5fe5e8ebfa65:0xeee27d959e262140",
#     "0x865c5f52c3dd74d9:0x5729ad78e3beccd1",
#     "0x865cf5f9b3b1d985:0x85c2fca497e47171",
#     "0x865c5fa2cb8d86c5:0x9bb457e1503ceed7",
#     "0x865c59026573d3bf:0x563396bb7a256944",
#     "0x865c67f288a36197:0xdfcbdcc6db72c68c",
#     "0x865c5f8452c5775b:0x974e68a19ff36670",
#     "0x865c5e5574533059:0x37c1c8689861e9bf",
#     "0x865cf5f90e74ea15:0x968da5eed67b1ba9",
#     "0x865c8b369a9e8241:0x20720b3848e06128",
#     "0x865c5f54cf190c6b:0xf364e668ceb5b329",
#     "0x865c58ac9c1be4f1:0xd2ac571e157b5e95",
#     "0x865c58bb2e990ded:0x6ede6270fd33d7d0",
#     "0x865c583a603af607:0x4dbd4449fcfe5778",
#     "0x865c6060a3902e61:0x7995b25ed7846bf3",
#     "0x865c5983a09261c3:0xfa80a68fb73fb089",
#     "0x865cf48c2fcf1213:0x33158e4095b2f305",
#     "0x865c92beaeb624eb:0x774466df2b8881fd",
#     "0x865c58ab335e4621:0x913a53749734d52",
#     "0x865c42631a2ca86b:0xf1b5db4cda259f9f",
#     "0x865c42e6bd420477:0xa9fc9c8c8809a9ba",
#     "0x865cf5f6849122a3:0xc9738af5f965e1d7",
#     "0x865c5f562195e129:0xe6e3a53342f7eee3",
#     "0x865ce8000e5fe115:0x7c6993b354be3e1d",
#     "0x865c58bec1fe0413:0x17629bc4e3dfa89",
#     "0x865c58acce08a011:0xf1c854a1b63834cd",
#     "0x865c61d4a5d38277:0xab0fa6bce1351b17",
#     "0x865c5b6e3c7de7e1:0xd5cce0ed99381b3d",
#     "0x865cf560fb9e27ed:0xd1c94573dc4558df",
#     "0x865cf6002e7fcf77:0xa776ce92eba1ee07",
#     "0x865c65558467eaf1:0x82799c6a853f36bb",
#     "0x865c604404f9a1c9:0x6a4db13f04589902",
#     "0x865c5f5559247a5b:0x8488331ff1b6f4c",
#     "0x865cf58ce8f088e9:0xf5cf102d1f662829",
#     "0x865c688ee2bf0b1d:0x1589e6cd2f7ad3d2",
#     "0x865c8acb8a8256a1:0xcb31ae316dc27ebb",
#     "0x865c58ab23859379:0xeabd07002a64cc5",
#     "0x865cf776ff084da9:0xcdbc48259c918589",
#     "0x865c60e50f343cd3:0xa42666e44329ffe9",
#     "0x865c5d3e930a88ef:0xf21967fcffda05cd",
#     "0x865c5d9580f877cd:0x12a3804f565f4849",
#     "0x865cf5fbfa67a0ed:0xb86ab3f02cd8bd1e",
#     "0x865c5f5e273c2f5f:0x7db915b5021e76ea",
#     "0x865c5d1a2e5cca49:0xc186b7b08e7eac0a",
#     "0x865c60052ce2e497:0xc48eff2ec9207d90",
#     "0x865c5f53f843d6b7:0x29beec82e4917223",
#     "0x865c5f54a9b7ebe7:0xa540c4c3341f73f3",
#     "0x865c43dd75e33ed5:0xf2f6bd252923ff2f",
#     "0x865c8b4015960359:0x526e8528e8529d47",
#     "0x865c5ff64aaf6da1:0xdf015503bdde947c",
#     "0x865cf389100cfadd:0x4d035451d6fac69e",
#     "0x865c427c4ca78a57:0xeece4c6c77d9f91f",
#     "0x865c8b4191243c9d:0xf4f83856c847c7d2",
#     "0x865cf5fed3b750a7:0x355bdb03632f2d77",
#     "0x865c5fe42365a02f:0xc7912a469b8545b5",
#     "0x865c58acae6fb6bf:0x7bf36035eb8a476e",
#     "0x865cf19bb415247b:0xaf29f4a581b6966d",
#     "0x865c5f2724a86b27:0xc7ac111244e4c333",
#     "0x865c588aef652825:0xe4841eb034314676",
#     "0x865cf5f68dbc614b:0x142b72b409d40b2d",
#     "0x865cf3a73ad80e9f:0x6b12708c17a2d347",
#     "0x865c682eeb15fe1b:0xb4d1038a6fd282af",
#     "0x865c596f264afda7:0x66e42cebac1f64ad",
#     "0x865c8ab0163d099f:0x96b212caf3b6952c",
#     "0x865c59f54299cf3f:0x2ea9a243bf8c1e1c",
#     "0x865c5db860843723:0x5f078714701f4150",
#     "0x865c5f644638122b:0xb74d041b4bf460e8",
#     "0x865cf55e6330460d:0x4b31cd07d7600c0e",
#     "0x865c5e29c8cb8383:0x3de03c2bf716a79d",
#     "0x865c58acae49bbd9:0xa16f7bdfd53ccb02",
#     "0x865c5e1a9d8efb8b:0xe5a1f202727f798a",
#     "0x865cf5416527b18b:0xabeeae06f689b1af",
#     "0x865cf1357baaa3b3:0x48bd7879cbf43932",
#     "0x865c5917d5da613f:0xc423c28005b5fd88",
#     "0x865c8a9349d530e5:0x5c1097f5256446f8",
#     "0x865c59425cf39983:0xc9d107eab6f0e994",
#     "0x865c69e3442f9883:0xfa2aebb714dc9bc3",
#     "0x865cf5736bc53883:0x9ef1fed37c870c03",
#     "0x865c8d19468c1e3d:0x12f62f8941742a0b",
#     "0x865c600b2b129ee7:0xa59cb05601631d52",
#     "0x865c592b3662db8f:0x2ae75bda718cb007",
#     "0x865c43330aa74da9:0x40c28a6c21223507",
#     "0x865cf54926d124ff:0xecf5180844199d10",
#     "0x865c5b0f9c37eb5b:0xa4a1ec6c874d4b9a",
#     "0x865cf6074d2b5bfb:0xda568226932472dd",
#     "0x865c6887ed92a9b1:0xb089120bde3d4410",
#     "0x865cf5423076ef63:0x930d9c688d578551",
#     "0x865c43ab9c05b319:0x84b3760b33cb67bc",
#     "0x865c58aab15e6409:0xc6a6c6bee8b011cd",
#     "0x865c5d95d011fa31:0xef6ab0315e8b0bae",
#     "0x865cf620384d453d:0xe4064c8964286c11",
#     "0x865c5c450169f0ff:0xd6e00c64709438e6",
#     "0x865c5f3fd1e73417:0x390b5400d4d6ca93",
#     "0x865c58ad053e4955:0x54e1daf67e2d8967",
#     "0x865cf4aa20eaaaa5:0x31c8910f683879c8",
#     "0x865c5f53f85ba6af:0xc0a5feb837a8e49e",
#     "0x865cf560defb759b:0x58b445709ff0afb9",
#     "0x865c589e74898b07:0xad32537c3419e985",
#     "0x865c6007df646e79:0xb14f7f5e6a8f845",
#     "0x865c5993e80f4e87:0xb810d8d43f2cfea2",
#     "0x865c58ab94e57861:0x7ac07f81384336bb",
#     "0x865c5feeed929c47:0xf0055cf6392e0c24",
#     "0x865c596d4da4b2c5:0xa02e4da3630ed62a",
#     "0x865c5e6deea239c5:0x8158a7210c855b65",
#     "0x865c5f609bb86ef1:0xc1527d4fc7f90378",
#     "0x865c61d4c9e34ff3:0xdde440520d07eeed",
#     "0x865c5d25bd786c11:0xb14fa975a3973ecc",
#     "0x865c5aa70b64d22f:0x4b8007faf6b35367",
#     "0x865cf4858c57812f:0x3f7367520a5a9007",
#     "0x865cf59fe42b6abd:0xbe16214491543e1d",
#     "0x865c614e01eb37a3:0x1bb7887022031750",
#     "0x865cf4e21a78ab17:0x246c332e98c3df77",
#     "0x865cf54ad9a4c1bf:0x2804969fdba7b647",
#     "0x865c5f694b3fe6d9:0xa02c39fa6c4efe9c",
#     "0x865c14392b631bcb:0x11daa71660447efa",
#     "0x865cf4e8801c244f:0xc784a466e472bca7",
#     "0x865c8b317cdb3fd7:0xb7aa81ab00a4a161",
#     "0x865c5a4c64c321bf:0x269f19afb8d2ad0d",
#     "0x865c5fef1b1eb28b:0x28d8b21124250959",
#     "0x865c58bb119aca07:0xf84a783b51a3cc50",
#     "0x865c58ab645a4e31:0x5803ce6b3bd20d24",
#     "0x865c688631226d4d:0x214a9fa3eae7052f",
#     "0x865c8b089574e5f9:0x5f6cdad29e0ce6d6",
#     "0x865c6766df139545:0xb528f882ffdade6c",
#     "0x865c66de784d0995:0x1cc59d3d9b49d55",
#     "0x865c42cb790f990f:0x206f810edbf15d83",
#     "0x865c42b15a7462a9:0xdab3e1ee7c69976e",
#     "0x865c8b66091e60af:0xbfb7b8aedb690aeb",
#     "0x865c5f27aba7e963:0x531cb565ca608308",
#     "0x865c678960b867d3:0x174d7c40b90a0efa",
#     "0x865c58263fbd147f:0x9076e75208fe71c0",
#     "0x865c5a5ccb64edb3:0x39f6a3f12e7fa4a6",
#     "0x865cf5f870cd0e51:0xcc9a9b0b33751b97",
#     "0x865cf620dbf4a387:0x61a41a7af2c156a9",
#     "0x865c93e9b402f183:0x4d8789e0db6a1e73",
#     "0x865cf5f3d5095555:0xf1a82edf4c62d9d2",
#     "0x865c58ab22d35a13:0x9211f88fbda9e925",
#     "0x865c60beef467e11:0x41030479acaa140f",
#     "0x865c60b105202a17:0xe59b66d4c5e1911",
#     "0x865cf52d0d3c0113:0x305ca740beaf16ad",
#     "0x865c8d695e628c39:0xfe208b74647960d3",
#     "0x865c5847d5881531:0x89e0f1785c8ba9ef",
#     "0x865c3efc159afacf:0xa90611762f7982f8",
#     "0x865c9333ffd7b73f:0xc9259ce5b64c25d0",
#     "0x865c6011e6df9059:0x1279f4895e0024ba",
#     "0x865cf79bcb2a15cf:0x20b7c82393c68121",
#     "0x865c58af2aedb861:0xc211f5355a02f6af",
#     "0x865c8acada673de7:0x5af30d9d4a90b02b",
#     "0x865c58acca18d24b:0x19b0d017193e1179",
#     "0x865c8b33d3719feb:0x6b9b34b3d1f4ffd0",
#     "0x865c8bbaf016a135:0x8db664b422074404",
#     "0x880e2d79bdb3521f:0x3629a8f540928fe6",
#     "0x865c430a8d5067e9:0xddb5ef84bbad789c",
#     "0x865cf606b46ae265:0x6fc4d6a10edbe486",
#     "0x865c600b015723e5:0xf3ce8abddc8b764",
#     "0x865cf33986cbdf4d:0xb2de82916ccaadbd",
#     "0x865cf55e045b3b31:0xca653544b3f8f04c",
#     "0x865cf7ff42b44eb3:0xbd201ccf5ef9c167",
#     "0x865c679f46d4efd3:0x6aee3b33a2dfd3b5",
#     "0x865c420cc381d815:0x831219fb3f46f47d",
#     "0x865c5fc0684d96f1:0x4d410d0a1257f5f6",
#     "0x865c5ff91d942399:0x580359f4d26ee8b4",
#     "0x865c6887d6c2a48d:0x1b51024fc641b0da",
#     "0x865cf4548e25ab8b:0xe737bf4117d395ce",
#     "0x865c58bb2fb7e8d3:0x7254d7209ee5b893",
#     "0x865cf5f6911669b3:0x42c47ebb9d05e2e9",
#     "0x865c8b6eeb2746f1:0xafdbc2247cb2e5e4",
#     "0x865c58a63d0da53b:0xc45817dfa7b37585",
#     "0x865c5e03cb6c3b73:0x833c4571249a243d",
#     "0x865c9366afb717ed:0x7fd3c63aa0fc1e92",
#     "0x865c59c95b7963f3:0xe6bdfa0ba82588ef",
#     "0x145dcc43b931d4df:0xd8b4a0cdd9677687",
#     "0x865c6011d1eb8a47:0xe9e9c874de19853a",
#     "0x865c8ab1b8878d8f:0x551622bbc21b6756",
#     "0x865c5d95835bc411:0x940024fbdf46b470",
#     "0x865cf5493edb6f75:0x4a1a4fc45b3f0911",
#     "0x865c5ee74deaebb1:0x136f416dc19512ec",
#     "0x865c5f604aa87989:0x928640d6925c104e",
#     "0x865cf5f8c686d547:0xa8007e8cdd82f6c",
#     "0x865cf2923c71af0b:0x1247cdca6450f289",
#     "0x865c6752dbcb1fbb:0x5bbeed182aeddc18",
#     "0x865c5914b8f80169:0x2ba985fa9322e43c",
#     "0x865cf787152d4dc9:0xaaf6d80d04d7b652",
#     "0x865c60b6e07e5463:0xc26b38ab17d4be91",
#     "0x865c5fe2b1a26155:0xeeb2754363329043",
#     "0x865cf4a746072d39:0x1de010188719d21",
#     "0x865c5d6290c356ad:0x2c849bf1681ac6ea",
#     "0x865c5de03d80f229:0xa98b6528ee29a679",
#     "0x865cf7e184254f81:0x74affd80276e9ced",
#     "0x865c66dfa6f129e3:0x50281861a73b0896",
#     "0x865cb81e46d91b6f:0xc73791424c5d392a",
#     "0x865cf606cae71445:0x67a0ca10beede299",
#     "0x865c3efc159afacf:0xf43729900cc2f605",
#     "0x865c5f54b732a4dd:0x3f9fde9b19b0bf9c",
#     "0x865c5f272bee0d59:0xfc89cfe0396dae70",
#     "0x865c58aa9dad2cd3:0x819432cf08ac8c39",
#     "0x865cf5b765ef05f9:0x5b81c4963014676",
#     "0x865c5c44f9ee749b:0x383c57a131b12936"
# ]
#     from apps.places.models.places import Place
#     known = set(Place.objects.filter(tfid__in=tfids).values_list('id', flat=True))
#     tfids = list(set(tfids).difference(known))
#     print(len(tfids))
    tfids = []
    Maps().local_scan(latitude=lat,
                      longitude=long,
                      keywords=MAP_KEYWORDS,
                      tfids=tfids)


def flatten_lists(list_):
    return set([i for sublist in list_ for i in sublist])


class Maps(object):
    timeout = 15
    zoom = 150000
    user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) "
                                "Chrome/54.0.2840.98 Safari/537.36"}

    def __init__(self, debug=True, use_proxies=True):
        if use_proxies:
            self.proxy = Proxy()
        else:
            self.proxy = requests
        self.debug = debug

    def get_place_details(self, tfid: str, lat: str, long: str):
        params_url = {
            "authuser": "0",
            "hl": "en",
            "tch": 1,
            "q": tfid,
            "pb": f"!1m14!1s{tfid}!3m12!1m3"
            f"!1d{self.zoom}"
            f"!2d{long}"
            f"!3d{lat}"
            f"!2m3!1f0!2f0!3f0!3m2!1i3440!2i661!4f13.1!12m4!2m3!1i360!2i120!4i8!13m57!2m2!1i203"
            f"!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0"
            f"!3e3!1m3!1e3!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e3!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2"
            f"!1m3!1e10!2b0!3e4!2b1!4b1!9b0!14m3"
            f"!1s"
            f"!2z"
            f"!7e81"
            f"!15m49!1m13!4e1!13m6!2b1!3b1!4b1!6i1!8b1!9b1!18m4!3b1!4b1!5b1!6b1!2b1!5m5!2b1!3b1!5b1!6b1!7b1!10m1"
            f"!8e3!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!30m1!2b1!36b1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5"
            f"!3m4!1m3!1m2!1i224!2i298"
            # f"!21m28!1m6!1m2!1i0!2i0!2m2!1i458!2i661!1m6!1m2!1i3390!2i0!2m2!1i3440!2i661!1m6"
            # f"!1m2!1i0!2i0!2m2!1i3440!2i20!1m6!1m2!1i0!2i641!2m2!1i3440!2i661"
            f"!22m1!1e81!29m0!30m1!3b1"
        }

        resp = self.proxy.get("https://www.google.com/maps/preview/place", params=params_url, headers=self.user_agent,
                              timeout=self.timeout)
        if resp.status_code == 200:
            data = json.loads(resp.text[4:])
            tags = [item for sublist in self.index_get(data, 6, 76, default_return=[], null_override=[])
                    for item in sublist]
            if not tags or not set(tags).intersection(set(flatten_lists([x['tags'] for x in FILTERABLE_TAGS]))):
                return
            coordinates = dict(latitude=self.index_get(data, 4, 0, 2), longitude=self.index_get(data, 4, 0, 1),
                               offset=self.index_get(data, 4, 0, 0))

            address_list = self.index_get(data, 6, 2)
            try:
                city, tmp = address_list[-1].split(',')
                state, zip_code = tmp.split()
                address_ = ", ".join(address_list[:-1])
            except (TypeError, ValueError):
                city = None
                state = None
                zip_code = None
                address_ = None

            address = dict(address=address_, city=city, state=state,
                           zip_code=zip_code, neighborhood=self.index_get(data, 6, 14),
                           located_in=self.index_get(data, 6, 93, 0, 0, 0, 0),
                           located_in_tfid=self.index_get(data, 6, 93, 0, 0, 0, 1),
                           formatted_address=self.index_get(data, 6, 39))
            phone_numbers = [dict(display=x[0], normalized=x[1]) for x in
                             zip(self.index_get(data, 6, 3, null_override=[], default_return=[]),
                                 self.index_get(data, 6, 90, null_override=[], default_return=[]))]

            reviews = dict(link=self.index_get(data, 6, 4, 3, 0),
                           count=self.index_get(data, 6, 4, 8),
                           rating=self.index_get(data, 6, 4, 7),
                           displayed=[], extra=[])
            name = self.index_get(data, 6, 11)
            timezone = self.index_get(data, 6, 30)

            [
                reviews['displayed'].append(dict(comment=x[1], reviewer_pic=x[6][1][3]))
                for x in self.index_get(data, 6, 31, 1, default_return=[], null_override=[])
            ]
            hours = []
            tmp_hours = self.index_get(data, 6, 34) if self.index_get(data, 6, 34) is not None else []
            if tmp_hours:
                hours = [dict(day=x[0], hours_list=x[1]) for x in self.index_get(tmp_hours[1:], 0,
                                                                                 default_return=[],
                                                                                 null_override=[])]

            google = dict(tfid=tfid, place_map_link=self.index_get(data, 6, 42))
            pictures = [x[6][0] for x in self.index_get(data, 6, 51, 0, default_return=[], null_override=[]) if x[6]]
            if not pictures:
                pictures = [x[6][0] for x in self.index_get(data, 6, 72, 0, default_return=[], null_override=[]) if
                            x[6]]
            detailed_reviews = [dict(when=x[1], comment=x[3], stars=x[4],
                                     images=[y[6][0] for y in x[14]] if x[14] else []) for x in
                                self.index_get(data, 6, 52, 0, default_return=[], null_override=[])]
            # 2362

            popular_times = self.index_get(data, 6, 84, 0)
            popularity_and_wait_times = self.get_popularity_for_day(popular_times)

            # current_popularity is also not available if popular_times isn't
            current_popularity = self.index_get(data, 84, 7, 1)
            about = {}
            about_data = self.index_get(data, 6, 100, 1)
            if isinstance(about_data, list):
                for index, item in enumerate(about_data):
                    key = item[1]
                    for entry in item[2]:
                        if key not in about:
                            about[key] = []
                        about[key].append(dict(poi=entry[0], key=entry[1]))
            return dict(
                name=name,
                coordinates=coordinates,
                address=address,
                phone_numbers=phone_numbers,
                reviews=reviews,
                timezone=timezone,
                hours=hours,
                google=google,
                pictures=pictures,
                detailed_reviews=detailed_reviews,
                tags=[x.lower() for x in tags],
                popularity_and_wait_times=popularity_and_wait_times,
                current_popularity=current_popularity,
                about=about
            )

        else:
            raise Exception(f"Resp Code: {resp.status_code}.  \n {resp.request.url}\n{resp.text}")

    def do_search(self, lat: str, long: str, keyword: str, page: int = 0):
        screen_width = 3440
        screen_height = 800
        params_url = {
            "tbm": "map",
            "authuser": "0",
            "hl": "en",
            "tch": 0,
            "ech": page,
            "q": keyword,
            "pb": "!4m12!1m3"
            f"!1d{self.zoom}"
            f"!2d{long}"
            f"!3d{lat}"
                  "!2m3!1f0!2f0!3f0!3m2"

            f"!1i{screen_width}"
            f"!2i{screen_height}"
            f"!4f13.1!7i20!8i{page * 20}"
            f"!10b1!12m8!1m1!18b1!2m3!5m1!6e2!20e3!10b1!16b1!19m4!2m3!1i360!2i120!4i8!20m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e3!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e3!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m5!1s8eqZXq3qCc-7tgXXz5SAAw!4m1!2i5600!7e81!12e30!24m48!1m12!13m6!2b1!3b1!4b1!6i1!8b1!9b1!18m4!3b1!4b1!5b1!6b1!2b1!5m5!2b1!3b1!5b1!6b1!7b1!10m1!8e3!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!30m1!2b1!36b1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!26m4!2m3!1i80!2i92!4i8!30m28!1m6!1m2!1i0!2i0!2m2!1i458"
            f"!2i{screen_height}!1m6!1m2!1i3390!2i0!2m2"
            f"!1i{screen_width}!2i{screen_height}"
                  "!1m6!1m2!1i0!2i0!2m2"
            f"!1i{screen_width}!2i20!1m6!1m2!1i0!2i781!2m2"
            f"!1i{screen_width}!2i{screen_height}!31b1!34m13!2b1!3b1!4b1!6b1!8m3!1b1!3b1!4b1!9b1!12b1!14b1!20b1!23b1!37m1!1e81!42b1!46m1!1e9!47m0!49m1!3b1"
            # f"!50m65"
            # f"!1m60"
            f"!50m33"
            f"!1m28"
            f"!1m5!1u17!2m3!2m2!17m1!1e2"
            f"!2m7!1u17!4sSort+by+distance!5e1"
            f"!9s"
            f"!10m2!17m1!1e2"
            # f"!2m7!1u3!4sOpen+now!5e1!9s0ahUKEwjzr-_3gvDoAhUCNKwKHVSKBfUQ_KkBCMgHKBg!10m2!3m1!1e1"
            # f"!2m7!1u2!4sTop+rated!5e1!9s0ahUKEwjzr-_3gvDoAhUCNKwKHVSKBfUQ_KkBCMkHKBk!10m2!2m1!1e1"
            # f"!2m7!1u1!4sCheap!5e1!9s0ahUKEwjzr-_3gvDoAhUCNKwKHVSKBfUQ_KkBCMoHKBo!10m2!1m1!1e1"
            # f"!2m7!1u1!4sUpscale!5e1!9s0ahUKEwjzr-_3gvDoAhUCNKwKHVSKBfUQ_KkBCMsHKBs!10m2!1m1!1e2"
            f"!3m6!1u17!2m4!1m2!17m1!1e2!2sDistance!3m1!1u3!3m1!1u2!3m1!1u1!4BIAE!2e2!3m2!1b1!3b0!59BQ2dBd0Fn!65m0"

        }
        resp = self.proxy.get("https://www.google.com/search", params=params_url, headers=self.user_agent,
                              timeout=self.timeout)
        tfids = []
        if resp.status_code == 200:
            tfids, next_page = self.__parse_paged_results(resp)
            if next_page:
                tfids += self.do_search(lat, long, keyword, next_page)
        return tfids

    def search(self, lat: str, long: str, keywords: List[str], pool_class=Pool):
        print(f"Starting search for Lat/Long ({lat}/{long}) for keywords: {keywords}")
        start = time.time()
        tfids = []
        with pool_class(processes=10) as pool:
            tfids += pool.starmap(self.do_search, [[lat, long, x] for x in keywords])
        tfids = list(set([item for sublist in tfids for item in sublist]))

        if self.debug:
            search_time = time.time() - start
            with open('search-time.txt', 'w') as f:
                f.write(f'search time: {search_time}')
            with open('tfids.json', 'w') as f:
                json.dump(tfids, f, indent=4)
        return tfids

    def __parse_paged_results(self, response):
        parser = re.match(r'{"c":0,"d":"\)]}.*?(\[.*?),"e":.*"u":(".*?")}', response.text)
        current_page = re.match(r'.*&ech=(.*?)&', response.request.url)
        data = json.loads(json.loads('"' + parser.group(1)))
        records = data[0][1]
        results = [x for x in [self.__parse_paged_record(record) for record in records] if x]
        next_page = None
        if results:
            next_page = int(current_page.group(1)) + 1
        return results, next_page

    def __parse_paged_record(self, record):
        try:
            data = record[14]
        except IndexError:
            return None
        else:
            if not data:
                return None
        tfid = self.index_get(data, 10)
        # coordinates = dict(latitude=data[9][2], longitude=data[9][3])
        # name = data[11]
        # other_search_terms = data[13]
        # tags = data[76]
        return tfid

    def index_get(self, array, *argv, default_return=None, null_override=None):
        try:

            for index in argv:
                array = array[index]
            if array is None:
                return null_override
            return array

        # there is either no info available or no popular times
        # TypeError: rating/rating_n/populartimes wrong of not available
        except (IndexError, TypeError):
            if null_override:
                return null_override
            return default_return

    def get_popularity_for_day(self, popularity):
        """
        :param popularity:
        :return:
        """
        pop_json = [[0 for _ in range(24)] for _ in range(7)]
        wait_json = [[[0, "Closed"] for _ in range(24)] for _ in range(7)]
        popularity = popularity if popularity else []
        for day in popularity:

            day_no, pop_times = day[:2]

            if pop_times is not None:
                for el in pop_times:

                    hour, pop, wait_str = el[0], el[1], el[3],

                    pop_json[day_no - 1][hour] = pop

                    wait_l = [int(s) for s in wait_str.replace("\xa0", " ").split(" ") if s.isdigit()]
                    wait_json[day_no - 1][hour] = 0 if len(wait_l) == 0 else wait_l[0]

                    # day wrap
                    if hour == 23:
                        day_no = day_no % 7 + 1

        # {"name" : "monday", "data": [...]} for each weekday as list
        result_dict = {}
        for d in range(7):
            popularity = pop_json[d]
            wait_time = [x if isinstance(x, int) else x[0] for x in wait_json[d]]
            # result_dict[list(calendar.day_name)[d]] = list(zip(popularity, wait_time))
            result_dict[d] = list(zip(popularity, wait_time))

        return result_dict

    def insert_places(self, records):
        from apps.places.models.places import Place, About, AboutItem, Tag, PlaceHour, PhoneNumber, Address, Popularity, \
            Picture, Review, HighlightedReview

        def get_diff(list1, list2):
            existing = set(list1)
            items_ = set(list2)
            return existing.difference(items_) or items_.difference(existing)

        places_list = []
        tags_list = []
        pois_list = []
        for x in records:
            places_list.append(x['google']['tfid'])
            tags_list.append(x['tags'])
            for header, items in x['about'].items():
                pois_list.append([x['poi'] for x in items])
        places = {x.tfid: dict(place=x, created=False, record=None) for x in
                  Place.objects.filter(tfid__in=places_list)
                      .prefetch_related('tags', 'about', 'about__items', 'phone_number', 'place_hour', 'pictures',
                                        'highlighted_reviews', 'popularity')
                      .select_related('address', 'review')}
        tags = {x.name: x for x in Tag.objects.filter(name__in=flatten_lists(tags_list))}
        about_items = {x.poi: x for x in AboutItem.objects.filter(poi__in=flatten_lists(pois_list))}

        new_tags = set()
        new_records = {}
        new_about_items = []
        new_about_items_tmp = set()
        for data in records:
            if not places.get(data['google']['tfid']):
                new_records[data['google']['tfid']] = dict(place=Place(name=data['name'], tfid=data['google']['tfid'],
                                                                       maps_link=data['google']['place_map_link'],
                                                                       timezone=data['timezone'],
                                                                       coordinates=Point(
                                                                           data['coordinates']['longitude'],
                                                                           data['coordinates']['latitude'],
                                                                           srid=4326)), record=data, created=True)
            else:
                places[data['google']['tfid']]['record'] = data
                data['coordinates'] = Point(data['coordinates']['longitude'],
                                            data['coordinates']['latitude'],
                                            srid=4326)
                data['tfid'] = data['google']['tfid']
                data['maps_link'] = data['google']['place_map_link']
                save_place = False
                for column in ['name', 'tfid', 'timezone', 'maps_link', 'coordinates']:
                    if getattr(places[data['google']['tfid']]['place'], column) != data[column]:
                        save_place = True
                        setattr(places[data['google']['tfid']]['place'], column, data[column])
                if save_place:
                    places[data['google']['tfid']]['place'].save()

            for tag in data['tags']:
                if tag not in tags:
                    new_tags.add(tag)

            for header, items in data['about'].items():
                for item in items:
                    if item['poi'] not in about_items and item['poi'] not in new_about_items_tmp:
                        new_about_items.append(AboutItem(display=item['key'], poi=item['poi']))
                        new_about_items_tmp.add(item['poi'])
        about_items.update({x.poi: x for x in AboutItem.objects.bulk_create(new_about_items)})
        tags.update({x.name: x for x in Tag.objects.bulk_create([Tag(name=x) for x in new_tags])})
        places.update({x.tfid: dict(place=x, created=new_records[x.tfid]['created'],
                                    record=new_records[x.tfid]['record']) for x
                       in Place.objects.bulk_create([x['place'] for x in new_records.values()])})

        relations = {
            'about': dict(model=About, records=[]),
            'address': dict(model=Address, records=[]),
            'phone_number': dict(model=PhoneNumber, records=[]),
            'place_hours': dict(model=PlaceHour, records=[]),
            'pictures': dict(model=Picture, records=[]),
            'review': dict(model=Review, records=[]),
            'highlight_review': dict(model=HighlightedReview, records=[]),
            'popularity': dict(model=Popularity, records=[]),
        }
        existing_about = About.objects.filter(place__in=[x['place'].id for x in places.values()]).prefetch_related(
            'items')
        existing_about_lookup = {}
        for about in existing_about:
            if about.place_id not in existing_about_lookup:
                existing_about_lookup[about.place_id] = []
            existing_about_lookup[about.place_id].append(about)

        for tfid, value in places.items():
            place = value['place']
            record = value['record']
            created = value['created']
            if created:
                place.tags.set([tags[x] for x in record['tags']])
                relations['address']['records'].append(
                    dict(obj=Address(
                        formatted_address=record['address']['formatted_address'],
                        address=record['address']['address'],
                        located_in=record['address']['located_in'],
                        located_in_tfid=record['address']['located_in_tfid'],
                        state=record['address']['state'],
                        city=record['address']['city'],
                        neighborhood=record['address']['neighborhood'],
                        zip_code=record['address']['zip_code']), create=True,
                        as_fk=dict(column='address', parent=place, fields=['formatted_address', 'address', 'located_in',
                                                                           'located_in_tfid', 'city', 'state',
                                                                           'neighborhood', 'zip_code'])))
                for number in record['phone_numbers']:
                    relations['phone_number']['records'].append(
                        dict(obj=PhoneNumber(number=number['display'],
                                             normalized=number['normalized'],
                                             place=place),
                             create=True))
                [relations['place_hours']['records'].append(
                    dict(obj=PlaceHour(**x), create=True)) for x in create_hour_dict(place, record)]
                [relations['pictures']['records'].append(
                    dict(obj=Picture(url=x, place=place), create=True)) for x in record['pictures']]

                relations['review']['records'].append(
                    dict(obj=Review(link=record['reviews']['link'], rating=record['reviews']['rating'],
                                    count=record['reviews']['count']), create=True,
                         as_fk=dict(column='review', parent=place,
                                    fields=['link', 'rating', 'count'])))

                [relations['highlight_review']['records'].append(
                    dict(obj=HighlightedReview(comment=x['comment'], user_picture=x['reviewer_pic'], place=place),
                         create=True)) for x in record['reviews']['displayed']]
                for day, hours in record['popularity_and_wait_times'].items():
                    for index, pair in enumerate(hours):
                        relations['popularity']['records'].append(
                            dict(obj=Popularity(popularity=pair[0], wait_time=pair[1],
                                                hour=index, day=day,
                                                place=place), create=True))

            else:

                if get_diff([tag.name for tag in place.tags.all()], [tags[x].name for x in record['tags']]):
                    place.tags.set([tags[x] for x in record['tags']], clear=True)

                tmp = []
                for day, hours in record['popularity_and_wait_times'].items():
                    for index, pair in enumerate(hours):
                        tmp.append(dict(popularity=pair[0], wait_time=pair[1],
                                        hour=index, day=day,
                                        place=place))

                if get_diff([f"{x.day}-{x.hour}-{x.wait_time}-{x.popularity}"
                             for x in place.popularity.all()],
                            [f"{x['day']}-{x['hour']}-{x['wait_time']}-{x['popularity']}" for x in tmp]):
                    place.popularity.all().delete()
                    [relations['popularity']['records'].append(dict(obj=Popularity(**x), create=True)) for x in tmp]

                if get_diff([x.normalized for x in place.phone_number.all()],
                            [x['normalized'] for x in record['phone_numbers']]):
                    place.phone_number.all().delete()
                    for number in record['phone_numbers']:
                        relations['phone_number']['records'].append(
                            dict(obj=PhoneNumber(number=number['display'],
                                                 normalized=number['normalized'],
                                                 place=place),
                                 create=True))

                if get_diff([x.comment for x in place.highlighted_reviews.all()],
                            [x['comment'] for x in record['reviews']['displayed']]):
                    place.highlighted_reviews.all().delete()
                    [relations['highlight_review']['records'].append(
                        dict(obj=HighlightedReview(comment=x['comment'], user_picture=x['reviewer_pic'], place=place),
                             create=True)) for x in record['reviews']['displayed']]

                tmp_data = create_hour_dict(place, record)
                if get_diff(
                        [f"{x.open_day}-{x.open_hour}-{x.closed_day}-{x.closed_hour}" for x in place.place_hour.all()],
                        [f"{x['open_day']}-{x['open_hour']}-{x['closed_day']}-{x['closed_hour']}" for x in tmp_data]):
                    place.place_hour.all().delete()
                    [relations['place_hours']['records'].append(
                        dict(obj=PlaceHour(**x), create=True)) for x in tmp_data]

                if not place.address:
                    relations['address']['records'].append(
                        dict(obj=Address(
                            formatted_address=record['address']['formatted_address'],
                            address=record['address']['address'],
                            located_in=record['address']['located_in'],
                            located_in_tfid=record['address']['located_in_tfid'],
                            state=record['address']['state'],
                            city=record['address']['city'],
                            neighborhood=record['address']['neighborhood'],
                            zip_code=record['address']['zip_code']), create=True,
                            as_fk=dict(column='address', parent=place,
                                       fields=['formatted_address', 'address', 'located_in',
                                               'located_in_tfid', 'city', 'state',
                                               'neighborhood', 'zip_code'])))
                else:
                    relations['address']['records'].append(
                        dict(obj=place.address, create=False,
                             as_fk=dict(column='address', parent=place, data=record['address'],
                                        fields=['formatted_address', 'address', 'located_in',
                                                'located_in_tfid', 'city', 'state',
                                                'neighborhood', 'zip_code'])))
                if not place.review:
                    if record['reviews']['count']:
                        relations['review']['records'].append(
                            dict(obj=Review(link=record['reviews']['link'], rating=record['reviews']['rating'],
                                            count=record['reviews']['count']), create=True,
                                 as_fk=dict(column='review', parent=place,
                                            fields=['link', 'rating', 'count'])))
                else:
                    relations['review']['records'].append(
                        dict(obj=place.review, create=False,
                             as_fk=dict(column='review', parent=place, data=record['reviews'],
                                        fields=['link', 'rating', 'count'])))

                if get_diff([x.url for x in place.pictures.all()], [x for x in record['pictures']]):
                    place.pictures.all().delete()
                    [relations['pictures']['records'].append(
                        dict(obj=Picture(url=x, place=place), create=True)) for x in record['pictures']]

            for header, items in record['about'].items():
                if place.id in existing_about_lookup:
                    existing_objs = [x for x in existing_about_lookup[place.id] if header == x.header]
                    if existing_objs:
                        relations['about']['records'].append(
                            dict(obj=existing_objs[0],
                                 create=False,
                                 many_to_manys=dict(model=AboutItem, column='items',
                                                    records=[about_items[x['poi']] for x in items]))
                        )
                    else:
                        relations['about']['records'].append(
                            dict(obj=About(header=header, place=place),
                                 create=True,
                                 many_to_manys=dict(model=AboutItem, column='items',
                                                    records=[about_items[x['poi']] for x in items]))
                        )
                else:
                    relations['about']['records'].append(
                        dict(obj=About(header=header, place=place),
                             create=True,
                             many_to_manys=dict(model=AboutItem, column='items',
                                                records=[about_items[x['poi']] for x in items]))
                    )

        for key, items in relations.items():
            objs = [x['obj'] for x in items['records'] if not x['create']]
            objs += items['model'].objects.bulk_create([x['obj'] for x in items['records'] if x['create']])
            for index, record in enumerate(objs):
                as_fk = items['records'][index].get('as_fk', {})
                if as_fk:
                    existing_fk = getattr(as_fk['parent'], as_fk['column'])
                    if existing_fk:
                        changes = [x for x in as_fk['fields'] if getattr(existing_fk, x) != as_fk['data'].get(x)]
                        if changes:
                            [setattr(existing_fk, change, as_fk['data'].get(change)) for change in changes]
                            existing_fk.save()
                    else:
                        setattr(as_fk['parent'], as_fk['column'], record)
                        as_fk['parent'].save()
                m2ms = items['records'][index].get('many_to_manys', {})
                if m2ms:
                    existing_items = set([x.id for x in getattr(record, m2ms['column']).all()])
                    record_items = set([x.id for x in m2ms['records']])
                    if existing_items.difference(record_items) or record_items.difference(existing_items):
                        getattr(record, m2ms['column']).set(record_items, clear=True)

        return [x['place'] for x in places.values()]

    def get_place_details_pool(self, latitude, longitude, tfids, pool_class=Pool):
        print(f"Starting detail lookup for Lat/Long ({latitude}/{longitude}) for tfids: {tfids}")
        with pool_class(processes=10) as pool:
            places = pool.starmap(Maps().get_place_details, [[x, latitude, longitude] for x in tfids])
        places = [x for x in places if x]
        if self.debug:
            start = time.time()
            detail_time = time.time() - start
            with open('detail-time.txt', 'w') as f:
                f.write(f'detail time: {detail_time}')
                f.write(f'count: {len(places)}')
            with open('places.json', 'w') as f:
                json.dump(places, f, indent=4)
        return places

    def bulk_insert(self, places, latitude, longitude, search_id):
        print(f"Starting inserts for Lat/Long ({latitude}/{longitude}) for {len(places)} places.")
        places = self.insert_places(places)
        from apps.places.models.places import PlaceSearch
        search = PlaceSearch.objects.get(id=search_id)
        search.places.add(*places)
        if not search.errored:  # Checks if None or False, it's a NO-OP if it's already False
            search.errored = False
        search.save()

    def local_scan(self, latitude, longitude, keywords: List[str], tfids=None):
        # from apps.places.models.places import PlaceSearch
        # search = PlaceSearch.objects.create(coordinates=Point(float(longitude), float(latitude), srid=4326))
        if not tfids:
            tfids = self.search(latitude, longitude, keywords)
        places = self.get_place_details_pool(latitude, longitude, tfids)
        import ipdb; ipdb.set_trace()
        # self.bulk_insert(places, latitude, longitude, search.id.hex)


if __name__ == "__main__":
    test()
    # scratch('0x8644b509a62afffb:0x9a161a36bc32df9d')
