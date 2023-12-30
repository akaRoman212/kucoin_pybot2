#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 22:47:41 2023

@author: raviraj
"""
import time
import pprint

from kucoin.client import Client



api_key = '6224bde70fd8a700019e8bc5'
api_secret = '327de38a-60ad-4606-898d-50f03d50c680'
api_passphrase = '85462500'


client = Client(api_key, api_secret, api_passphrase)


tokens = ['FET', 'XMR', 'ANKR', 'MTV', 'CRO', 'OPT', 'KMD', 'RFOX', 'TT', 'ATOM', 'CHR', 'NIM', 'OCEAN', 'COTI', 'FX', 'XTZ', 'BNB', 'JAR', 'ALGO', 'ADA', 'XEM', 'CIX100', 'ZEC', 'FORESTPLUS', 'BOLT', 'ARPA', 'CHZ', 'NOIA', 'EOSC', 'DERO', 'WIN', 'FKX', 'ENQ', 'THETA', 'ONE', 'TOKO', 'TFUEL', 'LOL', 'LUNA', 'VID', 'SXP', 'VIDT', 'AKRO', 'ROOBEE', 'AMPL', 'MAP', 'COS', 'KPOL', 'ARX', 'NWC', 'BEPRO', 'VRA', 'KSM', 'SUTER', 'ACOIN', 'VI', 'AXE', 'STEEM', 'SENSO', 'PRE', 'XDB', 'SYLO', 'WOM', 'CADH', 'JST', 'STX', 'COMP', 'KAI', 'DOT', 'EWT', 'WEST', 'NVT', 'BNS', 'ORN', 'PNK', 'WAVES', 'SUKU', 'MLK', 'DIA', 'SHA', 'LINK', 'USDJ', 'ALEPH', 'EFX', 'CKB', 'UMA', 'VELO', 'SUN', 'BUY', 'YFI', 'UNI', 'UOS', 'SATT', 'KTS', 'DEGO', 'RFUEL', 'UBX', 'FIL', 'REAP', 'AAVE', 'TONE', 'OPCT', 'UQC', 'SHR', 'ROSE', 'UST', 'CTI', 'ETH2', 'BUX', 'XHV', 'PLU', 'CAS', 'GRT', 'MSWAP', 'REVV', 'API3', 'SUSHI', 'UNFI', 'ALPA', '1INCH', 'HTR', 'FRONT', 'WBTC', 'HYDRA', 'MIR', 'DFI', 'FRM', 'CRV', 'BTC3L', 'BTC3S', 'ETH3L', 'ETH3S', 'GZIL', 'ZEN', 'CUDOS', 'MAP2', 'REN', 'LRC', 'KLV', 'BOA', 'QNT', 'BAT', 'DAO', 'DOGE', 'STRONG', 'TRIAS', 'CAKE', 'ORAI', 'LTX', 'ZEE', 'MASK', 'IDEA', 'PHA', 'SRK', 'SWINGBY', 'AVAX', 'DON', 'KRL', 'POLK', 'RNDR', 'RLY', 'ANC', 'SKEY', 'LAYER', 'TARA', 'XYM', 'DYP', 'PCX', 'ORBS', 'DSLA', 'FLUX', 'SAND', 'XCUR', 'VAI', 'DODO', 'PUNDIX', 'BOSON', 'HT', 'PDEX', 'LABS', 'STRK', 'PHNX', 'HAI', 'EQZ', 'FORTH', 'CGG', 'GHX', 'TOWER', 'ACE', 'STND', 'LOCG', 'FLY', 'CARD', 'XDC', 'CWS', 'ADA3S', 'SHIB', 'POLX', 'KDA', 'GOVI', 'ICP', 'CELO', 'STC', 'MATIC', 'OGN', 'OUSD', 'GLQ', 'TLOS', 'YOP', 'MXC', 'ERSDL', 'ADA3L', 'HOTCROSS', 'HYVE', 'DAPPX', 'FEAR', 'KONO', 'MAHA', 'UNO', 'PRQ', 'PYR', 'GLCH', 'XCAD', 'PROM', 'EOS3L', 'EOS3S', 'BCH3L', 'BCH3S', 'ELON', 'APL', 'DIVI', 'VEED', 'LSS', 'AGIX', 'LPOOL', 'VET3L', 'VET3S', 'LTC3L', 'LTC3S', 'POLS', 'KOK', 'ABBC', 'ZCX', 'NORD', 'GMEE', 'XAVA', 'AI', 'SFUND', 'IOI', 'NFT', 'MNST', 'DLTA', 'AIOZ', 'MARSH', 'CQT', 'HAPI', 'GENS', 'YFDAI', 'FORM', 'MODEFI', 'ARRR', 'SPHRI', 'ASD', 'LPT', 'BOND', '2CRZ', 'NEAR', 'OOE', 'DFYN', 'CFG', 'MUSH', 'SMT', 'AXS', 'CLV', 'ROUTE', 'KAR', 'DPET', 'PMON', 'ERG', 'LITH', 'SOL', 'SLP', 'XCH', 'HAKA', 'MTL', 'GALAX', 'CIRUS', 'TXA', 'QI', 'ODDZ', 'PNT', 'XPR', 'TRIBE', 'MOVR', 'MAKI', 'QRDO', 'WOO', 'WILD', 'OXT', 'BAL', 'STORJ', 'YGG', 'NDAU', 'SDAO', 'SKL', 'NMR', 'XRP3L', 'XRP3S', 'TRB', 'IXS', 'PBX', 'GTC', 'LUNA3L', 'LUNA3S', 'DYDX', 'EQX', 'RLC', 'XNL', 'HBAR', 'XPRT', 'EGLD', 'FLOW', 'DOGE3L', 'DOGE3S', 'NKN', 'SOL3L', 'SOL3S', 'MLN', 'DMTR', 'LINK3L', 'LINK3S', 'DOT3L', 'DOT3S', 'CTSI', 'ALICE', 'OPUL', 'ILV', 'BAND', 'FTT', 'DVPN', 'SKU', 'SLIM', 'DEXE', 'TLM', 'RMRK', 'RUNE', 'MATTER', 'C98', 'BLOK', 'SOLR', 'UNI3L', 'UNI3S', 'ATOM3L', 'ATOM3S', 'SIENNA', 'PUSH', 'WSIENNA', 'NTVRK', 'YLD', 'FLAME', 'FTM3L', 'FTM3S', 'AXS3L', 'AXS3S', 'AGLD', 'NAKA', 'REEF', 'TORN', 'TIDAL', 'INJ', 'MATIC3L', 'MATIC3S', 'BNB3L', 'BNB3S', 'ALPHA', 'VEGA', 'AR', 'PERP', 'SCLP', 'JASMY', 'CPOOL', 'LTO', 'SUPER', 'AURY', 'HERO', 'XED', 'SWASH', 'NEAR3L', 'NEAR3S', 'SUSHI3L', 'SUSHI3S', 'DREAMS', 'MTRG', 'QUICK', 'TRU', 'WRX', 'DATA', 'ISP', 'CERE', 'SHILL', 'HEGIC', 'ERN', 'PAXG', 'AAVE3L', 'AUDIO', 'AAVE3S', 'SAND3L', 'SAND3S', 'FTG', 'XTM', 'ENS', 'ATA', 'FXS', 'MNW', 'CWAR', 'VXV', 'DPR', 'SWP', 'PBR', 'ANT', 'ADX', 'TWT', 'OM', 'AVAX3L', 'AVAX3S', 'MANA3L', 'MANA3S', 'GLM', 'NUM', 'MONI', 'TRADE', 'VLX', '1EARTH', 'KAVA', 'LIKE', 'LIT', 'SFP', 'BURGER', 'ILA', 'CREAM', 'RSR', 'GODS', 'IMX', 'KMA', 'SRM', 'POLC', 'XTAG', 'VR', 'MNET', 'NGC', 'GALAX3L', 'GALAX3S', 'HARD', 'UNIC', 'POND', 'MDX', 'EPIK', 'NGL', 'KDON', 'PEL', 'KLAY', 'LINA', 'CREDI', 'TRVL', 'ARKER', 'XEC', 'BONDLY', 'LACE', 'HEART', 'UNB', 'H3RO3S', 'FORWARD', 'GAFI', 'KOL', 'CHMB', 'FALCONS', 'UFO', 'GEEQ', 'RACEFI', 'ORC', 'PEOPLE', 'ADS', 'SOS', 'WHALE', 'IOTA', 'CWEB', 'HNT', 'GGG', 'CLH', 'REVU', 'PLGR', 'GLMR', 'CTC', 'GARI', 'FRR', 'ASTR', 'ERTHA', 'FCON', 'ACA', 'MTS', 'ROAR', 'HBB', 'AMP', 'CVX', 'MJT', 'XNO', 'STARLY', 'WMT', 'RANKER', 'LAVAX', 'MARS4', 'METIS', 'WAL', 'BULL', 'SON', 'MELOS', 'APE', 'VSYS', 'ACT', 'AERGO', 'AMB', 'AOA', 'AVA', 'BAX', 'BCH', 'BCHSV', 'BTC', 'BTCP', 'CAPP', 'COV', 'CPC', 'CRPT', 'CVC', 'DAG', 'DAI', 'DASH', 'DCR', 'DENT', 'DGB', 'DOCK', 'ELA', 'ELF', 'ENJ', 'EOS', 'EPRX', 'ETC', 'ETF', 'ETH', 'ETN', 'FTM', 'GAS', 'GGC', 'GMB', 'GOD', 'IOST', 'IOTX', 'J8T', 'KAT', 'KCS', 'KEY', 'KNC', 'LOC', 'LOOM', 'LSK', 'LTC', 'LYM', 'MAN', 'MANA', 'MKR', 'NEO', 'NULS', 'OLT', 'OMG', 'ONG', 'ONT', 'PLAY', 'QKC', 'QTUM', 'R', 'REQ', 'SNX', 'SOUL', 'TEL', 'TIME', 'TRAC', 'TRX', 'TUSD', 'USDC', 'USDT', 'UTK', 'VET', 'VTHO', 'WAN', 'WAX', 'XLM', 'XRP', 'XYO', 'ZIL', 'ZRX', 'SOLVE', 'BTT', 'GMT', 'BICO', 'STG', 'LMR', 'LOKA', 'URUS', 'BNC', 'JAM', 'LBP', 'CFX', 'XCN', 'LOOKS', 'UPO', 'TITAN', 'SLCL', 'CEEK', 'T', 'VEMP', 'NHCT', 'FRA', 'ARNM', 'VISION', 'ALPINE', 'ZBC', 'WOOP', 'NYM', 'VOXEL', 'PSTAKE', 'SPA', 'RACA', 'DAR', 'SYNR', 'MV', 'XDEFI', 'HAWK', 'SWFTC', 'XWG', 'BRWL', 'TAUM', 'CELR', 'AURORA', 'ELITEHERO', 'POSI', 'SIN', 'COOHA', 'PLD', 'EPX', 'PSL', 'SYS', 'OVR', 'DG', 'BRISE', 'PLY', 'GST', 'AKT', 'FSN', 'GAL', 'FITFI', 'BSW', 'H2O', 'AUSD', 'GMM', 'BOBA', 'XRACER', 'BFC', 'BIFI', 'DFA', 'MBL', 'DUSK', 'CCD', 'USDD', 'SCRT', 'MLS', 'AFK', 'ACH', 'APE3L', 'APE3S', 'GMT3L', 'GMT3S', 'IHC', 'STORE', 'DOSE', 'LUNC', 'USTC', 'JASMY3L', 'JASMY3S', 'IDLENFT', 'OP', 'EVER', 'ICX', 'MOOV', 'USDP', 'WELL', 'CSPR', 'FORT', 'REV3L', 'WEMIX', 'OGV', 'OLE', 'LDO', 'CULT', 'RBP', 'SRBP', 'HIBAYC', 'HIPUNKS', 'FIDA', 'WOMBAT', 'FT', 'HIENS4', 'EGAME', 'STEPWATCH', 'HISAND33', 'XRD', 'PIKASTER2', 'DC', 'HIENS3', 'NEER', 'RVN', 'MC', 'PEEL', 'SDL', 'HIODBS', 'SWEAT', 'CMP', 'PIX', 'HIDOODLES', 'MPLX', 'ETHW', 'QUARTZ', 'PUMLX', 'HIMAYC', 'ACQ', 'RED', 'AOG', 'PRMX', 'XETA', '00', 'GEM', 'HIOD', 'KICKS', 'ASTROBOY', 'DERC', 'TRIBL', 'P00LS', 'GMX', 'POKT', 'APT', 'BBC', 'EUL', 'TON', 'HIMEEBITS', 'HISQUIGGLE', 'XCV', 'ECOX', 'HFT', 'MM', 'HIFIDENZA', 'AZERO', 'BEAT', 'CLUB', 'NRFB', 'HIGAZERS', 'NAVI', 'HIPENGUINS', 'CARE', 'ALT', 'HICLONEX', 'OAS', 'PRIMAL', 'HICOOLCATS', 'HIAZUKI', 'TEM', 'HIFLUF', 'OSMO', 'FLR', 'HIBIRDS', 'BDX', 'HIMFERS', 'SIMP', 'MAGIC', 'ASTRA', 'HIVALHALLA', 'SQUAD', 'RPL', 'HIRENGA', 'HIGH', 'KING', 'OP2L', 'OP2S', 'SHIB2L', 'SHIB2S', 'APT2L', 'APT2S', 'HIUNDEAD', 'AGIX2L', 'AGIX2S', 'GRT2L', 'GRT2S', 'GFT', 'FLOKI', 'HIFRIENDS', 'BLUR', 'WAXL', 'SSV', 'IGU', 'ACS', 'BLUR2L', 'BLUR2S', 'CSIX', 'HISEALS', 'CFX2L', 'CFX2S', 'SIDUS', 'GOAL', 'SYN', 'GRAIL', 'DPX', 'RDNT', 'AIPAD', 'GNS', 'HIBEANZ', 'BLZ', 'MINA', 'NXRA', 'HALO', 'HMND', 'HIFI', 'NOM', 'LQTY', 'STRAX', 'ARB', 'ID', 'ID3L', 'ID3S', 'ARB3S', 'ARB3L', 'BTCUP', 'BTCDOWN', 'ETHUP', 'ETHDOWN', 'AOS', 'MYRIA', 'SD', 'RLTM', 'KAGI', 'CGPT', 'SXPUP', 'SXPDOWN', 'MASKUP', 'MASKDOWN', 'DYDXUP', 'DYDXDOWN', 'OTK', 'RNDRUP', 'RNDRDOWN', 'STXUP', 'STXDOWN', 'LINAUP', 'LINADOWN', 'ZPAY', 'PZP', 'BABYDOGE', 'INJUP', 'INJDOWN', 'ETCUP', 'ETCDOWN', 'LOCUS', 'IRON', 'IZI', 'SUI', 'SUI3L', 'SUI3S', 'KAS', 'CTSIUP', 'CTSIDOWN', 'ICPUP', 'ICPDOWN', 'PEPE', 'PEPEUP', 'PEPEDOWN', 'CETUS', 'SUIP', 'AIDOGE', 'WOJAK', 'BOB', 'MONG', 'TURBO', 'KARATE', 'WLKN', 'LMWR', 'TURBOS', 'FLOKIUP', 'FLOKIDOWN', 'KAVAUP', 'KAVADOWN', 'LUNCUP', 'LUNCDOWN', 'ZILUP', 'WOOUP', 'ZILDOWN', 'WOODOWN', 'SUIA', 'FILUP', 'FILDOWN', 'LUNAUP', 'LUNADOWN', 'ARPAUP', 'ARPADOWN', 'ROSEUP', 'ROSEDOWN', 'FETUP', 'FETDOWN', 'OCEANUP', 'OCEANDOWN', 'ALGOUP', 'ALGODOWN', 'LADYS', 'RFD', 'HIBAKC', 'TENET', 'INFRA', 'VERSE', 'OBI', 'TSUGT', 'PIKA', 'XPLL', 'LAI', 'EDU', 'ORDI', 'COMBO', 'VOLT', 'SEI', 'TOMI', 'CANDY', 'PIP', 'OMN', 'VCORE', 'MMM', 'XEN', 'MAV', 'LBR', 'AURA', 'PENDLE', 'GAMMA', 'EGO', 'PEPE2', 'COMPUP', 'COMPDOWN', 'MKRUP', 'MKRDOWN', 'LYX', 'DCK', 'WLD', 'WLDUP', 'WLDDOWN', 'AIEPK', 'SPRINT', 'PERPUP', 'PERPDOWN', 'UNFIUP', 'UNFIDOWN', 'TRBUP', 'TRBDOWN', 'PYUSD', 'FRONTUP', 'FRONTDOWN', 'GLMRUP', 'GLMRDOWN', 'ISLM', 'ZELIX', 'BIGTIME', 'NTRN', 'ARKM', 'VRAUP', 'VRADOWN', 'STORJUP', 'STORJDOWN', 'LOOMUP', 'LOOMDOWN', 'OFN', 'TIA', 'KLUB', 'CYBER', 'MEME', 'TOKEN', 'SHRAP', 'ORDIUP', 'ORDIDOWN', 'POL', 'SATS', 'RPK', 'ATEM', 'ATOR', 'PYTH', 'ROOT', 'RATS', 'VRTX', 'MIND', 'KASUP', 'KASDOWN', 'TIAUP', 'TIADOWN', 'PYTHUP', 'PYTHDOWN', 'FLIP', 'BONK', 'POLYX', 'MNT', 'INSP', 'WORK', 'AUCTION', 'JTO', 'VANRY', 'BAKEUP', 'BAKEDOWN', 'SNS', 'DOVI', 'SEAM', 'FINC', 'GTT', '1000BONKUP', 'JTOUP', 'JTODOWN', 'BONKUP', 'BONKDOWN', 'IRL', 'SCPT', 'MNDE', 'COQ', 'SOLS', 'TAO', 'TURT', 'BIIS', 'GRAPE', 'ARTY', 'AA', 'MUBI', 'ZOOA', 'ANALOS', 'SEIUP', 'SEIDOWN', 'OPUP', 'OPDOWN', 'MYRO', 'SILLY', 'MOBILE', 'ROUP']
# currencies = client.get_currencies()


# for x in currencies:
#     tokens.append(x['currency'])
# pprint.pprint(currencies)

# pprint.pprint(currencies[0]['currency'])

# # #Get all symbols and then compare in excel
# for x in currencies:
#     print(x['currency'])

# # #For new token search by user choice
# input = input("Which symbol you want to search???")

up_token = []
# # #Get all symbols and then compare in excel
while True:
    symbol = client.get_currencies()
    
    up_token.clear()
    for x in symbol:
        up_token.append(x['currency'])

    # print (len(up_token))
    # print (len(tokens))
    
    if (len(tokens) != len(up_token)):
        
        print("New pair found!!!")
        for y in range(len(up_token)):
            if up_token[y] not in tokens:
                print(up_token[y])
                tokens.append(up_token[y])
                seconds = time.time()
                print(seconds)
                for x in symbol:
                    if x['currency'] == up_token[y]:
                        pprint.pprint(x)
                        break
                
                # try:
                    

                #     # sending message using telegram client
                #     tclient.send_message('exit127001', up_token[y])
                # except Exception as e:
                    
                #     # there may be many error coming in while like peer
                #     # error, wrong access_hash, flood_error, etc
                #     print(e)
        
        break
    
    print("Kucoin Searching..............")
    time.sleep(10)
