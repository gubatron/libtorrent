#!/usr/bin/env python3

import pathlib

header = (pathlib.Path(__file__).parent / ".." / "include" / "libtorrent_alerts.h").open("w+")

f = (pathlib.Path(__file__).parent / ".." / ".." / ".." / "include" / "libtorrent" / "alert_types.hpp").open()

header.write('''// generated by tools/gen_alert_header.py

#ifndef LIBTORRENT_ALERTS_H
#define LIBTORRENT_ALERTS_H

// alert types
enum alert_types_t {
''')

for l in f:
	l = l.strip()

	if '#define' in l: continue

	if not 'TORRENT_DEFINE_ALERT(' in l and \
		not 'TORRENT_DEFINE_ALERT_PRIO(' in l:
		continue

	args = l.split('(')[1].split(')')[0].split(',')
	args[0] = args[0].replace('_alert', '')

	header.write('	ALERT_%s = %s,\n' % (args[0].upper(), args[1]))

header.write('''};

#endif // LIBTORRENT_ALERTS_H
''')