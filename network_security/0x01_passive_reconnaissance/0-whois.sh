#!/bin/bash
DOMAIN="$1"
OUTPUT="${DOMAIN}.csv"

whois "$DOMAIN" | awk -F': +' '
BEGIN {
    # Tələb olunan bütün sahələri sıra ilə siyahıya alırıq
    fields[1] = "Registrant Name"
    fields[2] = "Registrant Organization"
    fields[3] = "Registrant Street"
    fields[4] = "Registrant City"
    fields[5] = "Registrant State/Province"
    fields[6] = "Registrant Postal Code"
    fields[7] = "Registrant Country"
    fields[8] = "Registrant Phone"
    fields[9] = "Registrant Phone Ext:"
    fields[10] = "Registrant Fax"
    fields[11] = "Registrant Fax Ext:"
    fields[12] = "Registrant Email"

    fields[13] = "Admin Name"
    fields[14] = "Admin Organization"
    fields[15] = "Admin Street"
    fields[16] = "Admin City"
    fields[17] = "Admin State/Province"
    fields[18] = "Admin Postal Code"
    fields[19] = "Admin Country"
    fields[20] = "Admin Phone"
    fields[21] = "Admin Phone Ext:"
    fields[22] = "Admin Fax"
    fields[23] = "Admin Fax Ext:"
    fields[24] = "Admin Email"

    fields[25] = "Tech Name"
    fields[26] = "Tech Organization"
    fields[27] = "Tech Street"
    fields[28] = "Tech City"
    fields[29] = "Tech State/Province"
    fields[30] = "Tech Postal Code"
    fields[31] = "Tech Country"
    fields[32] = "Tech Phone"
    fields[33] = "Tech Phone Ext:"
    fields[34] = "Tech Fax"
    fields[35] = "Tech Fax Ext:"
    fields[36] = "Tech Email"
}
{
    # whois çıxışından gələn Açar: Dəyər cütlərini oxuyuruq
    key = $1
    val = $2
    gsub(/^[ \t]+|[ \t]+$/, "", key)
    gsub(/^[ \t]+|[ \t]+$/, "", val)
    if (key != "") {
        data[key] = val
    }
}
END {
    total = 36
    for (i = 1; i <= total; i++) {
        f = fields[i]
        val = data[f]

        # Street sahələrinin sonuna boşluq əlavə olunur
        if (f ~ /Street$/ && val != "") {
            val = val " "
        }

        # CSV formatında çıxarış: Field,Value
        out = f "," val

        # Sonda artıq boş sətir (newline) olmamasını təmin edirik
        if (i < total) {
            printf "%s\n", out
        } else {
            printf "%s", out
        }
    }
}
' > "$OUTPUT"
