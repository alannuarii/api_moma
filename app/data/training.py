training_data = [
	{ 'pltd': 0, 'pv': 1, 'bss': 0, 'cuaca': 1, 'irr': 0, 'mode': '1PV' },
	{ 'pltd': 0, 'pv': 1, 'bss': 1, 'cuaca': 1, 'irr': 0, 'mode': '1PV-1BSS' },
	{ 'pltd': 1, 'pv': 1, 'bss': 1, 'cuaca': 1, 'irr': 0, 'mode': '1PV-1BSS' },
	{ 'pltd': 0, 'pv': 1, 'bss': 2, 'cuaca': 1, 'irr': 0, 'mode': '1PV-1BSS' },
	{ 'pltd': 1, 'pv': 1, 'bss': 2, 'cuaca': 1, 'irr': 0, 'mode': '1PV-1BSS' },
	{ 'pltd': 2, 'pv': 1, 'bss': 2, 'cuaca': 1, 'irr': 0, 'mode': '1PV-1BSS' },
	{ 'pltd': 0, 'pv': 2, 'bss': 0, 'cuaca': 1, 'irr': 0, 'mode': '1PV' },
	{ 'pltd': 0, 'pv': 2, 'bss': 1, 'cuaca': 1, 'irr': 0, 'mode': '1PV-1BSS' },
	{ 'pltd': 1, 'pv': 2, 'bss': 1, 'cuaca': 1, 'irr': 0, 'mode': '1PV-1BSS' },
	{ 'pltd': 0, 'pv': 2, 'bss': 2, 'cuaca': 1, 'irr': 0, 'mode': '2PV-2BSS' },
	{ 'pltd': 1, 'pv': 2, 'bss': 2, 'cuaca': 1, 'irr': 0, 'mode': '2PV-2BSS' },
	{ 'pltd': 2, 'pv': 2, 'bss': 2, 'cuaca': 1, 'irr': 0, 'mode': '2PV-2BSS' },
	{ 'pltd': 0, 'pv': 1, 'bss': 0, 'cuaca': 0, 'irr': 1, 'mode': '1PV' },
	{ 'pltd': 0, 'pv': 1, 'bss': 1, 'cuaca': 0, 'irr': 1, 'mode': '1PV-1BSS' },
	{ 'pltd': 1, 'pv': 1, 'bss': 1, 'cuaca': 0, 'irr': 1, 'mode': '1PV-1BSS' },
	{ 'pltd': 0, 'pv': 1, 'bss': 2, 'cuaca': 0, 'irr': 1, 'mode': '1PV-1BSS' },
	{ 'pltd': 1, 'pv': 1, 'bss': 2, 'cuaca': 0, 'irr': 1, 'mode': '1PV-1BSS' },
	{ 'pltd': 2, 'pv': 1, 'bss': 2, 'cuaca': 0, 'irr': 1, 'mode': '1PV-1BSS' },
	{ 'pltd': 0, 'pv': 2, 'bss': 0, 'cuaca': 0, 'irr': 1, 'mode': '1PV' },
	{ 'pltd': 0, 'pv': 2, 'bss': 1, 'cuaca': 0, 'irr': 1, 'mode': '1PV-1BSS' },
	{ 'pltd': 1, 'pv': 2, 'bss': 1, 'cuaca': 0, 'irr': 1, 'mode': '1PV-1BSS' },
	{ 'pltd': 0, 'pv': 2, 'bss': 2, 'cuaca': 0, 'irr': 1, 'mode': '2PV-2BSS' },
	{ 'pltd': 1, 'pv': 2, 'bss': 2, 'cuaca': 0, 'irr': 1, 'mode': '2PV-2BSS' },
	{ 'pltd': 2, 'pv': 2, 'bss': 2, 'cuaca': 0, 'irr': 1, 'mode': '2PV-2BSS' },
	{ 'pltd': 0, 'pv': 1, 'bss': 0, 'cuaca': 0, 'irr': 0, 'mode': '1PV' },
	{ 'pltd': 0, 'pv': 1, 'bss': 1, 'cuaca': 0, 'irr': 0, 'mode': '1PV-1BSS' },
	{ 'pltd': 1, 'pv': 1, 'bss': 1, 'cuaca': 0, 'irr': 0, 'mode': '1PV-1BSS' },
	{ 'pltd': 0, 'pv': 1, 'bss': 2, 'cuaca': 0, 'irr': 0, 'mode': '1PV-1BSS' },
	{ 'pltd': 1, 'pv': 1, 'bss': 2, 'cuaca': 0, 'irr': 0, 'mode': '1PV-1BSS' },
	{ 'pltd': 2, 'pv': 1, 'bss': 2, 'cuaca': 0, 'irr': 0, 'mode': '1PV-1BSS' },
	{ 'pltd': 0, 'pv': 2, 'bss': 0, 'cuaca': 0, 'irr': 0, 'mode': '1PV' },
	{ 'pltd': 0, 'pv': 2, 'bss': 1, 'cuaca': 0, 'irr': 0, 'mode': '1PV-1BSS' },
	{ 'pltd': 1, 'pv': 2, 'bss': 1, 'cuaca': 0, 'irr': 0, 'mode': '1PV-1BSS' },
	{ 'pltd': 0, 'pv': 2, 'bss': 2, 'cuaca': 0, 'irr': 0, 'mode': '2PV-2BSS' },
	{ 'pltd': 1, 'pv': 2, 'bss': 2, 'cuaca': 0, 'irr': 0, 'mode': '2PV-2BSS' },
	{ 'pltd': 2, 'pv': 2, 'bss': 2, 'cuaca': 0, 'irr': 0, 'mode': '2PV-2BSS' },
	{ 'pltd': 1, 'pv': 1, 'bss': 0, 'cuaca': 1, 'irr': 1, 'mode': '1PV' },
	{ 'pltd': 1, 'pv': 1, 'bss': 0, 'cuaca': 1, 'irr': 1, 'mode': '1PV-1BSS' },
	{ 'pltd': 1, 'pv': 1, 'bss': 1, 'cuaca': 1, 'irr': 1, 'mode': '1PV-1BSS-1ENGINE' },
	{ 'pltd': 0, 'pv': 1, 'bss': 2, 'cuaca': 1, 'irr': 1, 'mode': '1PV-1BSS' },
	{ 'pltd': 1, 'pv': 1, 'bss': 2, 'cuaca': 1, 'irr': 1, 'mode': '1PV-1BSS-1ENGINE' },
	{ 'pltd': 2, 'pv': 1, 'bss': 2, 'cuaca': 1, 'irr': 1, 'mode': '1PV-1BSS-1ENGINE' },
	{ 'pltd': 0, 'pv': 2, 'bss': 0, 'cuaca': 1, 'irr': 1, 'mode': '1PV' },
	{ 'pltd': 0, 'pv': 2, 'bss': 1, 'cuaca': 1, 'irr': 1, 'mode': '1PV-1BSS' },
	{ 'pltd': 1, 'pv': 2, 'bss': 1, 'cuaca': 1, 'irr': 1, 'mode': '1PV-1BSS-1ENGINE' },
	{ 'pltd': 0, 'pv': 2, 'bss': 2, 'cuaca': 1, 'irr': 1, 'mode': '2PV-2BSS' },
	{ 'pltd': 1, 'pv': 2, 'bss': 2, 'cuaca': 1, 'irr': 1, 'mode': '2PV-2BSS' },
	{ 'pltd': 2, 'pv': 2, 'bss': 2, 'cuaca': 1, 'irr': 1, 'mode': '2PV-2BSS-2ENGINE' }
]