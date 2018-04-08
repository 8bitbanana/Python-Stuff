# Invoice Creater for Crooks Design
# by Ethan Crooks

import pdfkit, datetime, os

TABLE_MARKER = "<!--TABLE-->"
TABLE_ENTRY = """

<tr class="item">
    <td>
        {:s}
    </td>
                
    <td>
        £{:,.2f}
    </td>
</tr>

"""

BASE_HTML = """

<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>[redacted] Invoice</title>
    
    <style>
    .invoice-box {
        max-width: 800px;
        margin: auto;
        padding: 30px;
        border: 1px solid #eee;
        box-shadow: 0 0 10px rgba(0, 0, 0, .15);
        font-size: 16px;
        line-height: 24px;
        font-family: Arial, sans-serif;
        color: #555;
    }
    
    .invoice-box table {
        width: 100%;
        line-height: inherit;
        text-align: left;
    }
    
    .invoice-box table td {
        padding: 5px;
        vertical-align: top;
    }
    
    .invoice-box table tr td:nth-child(2) {
        text-align: right;
    }
    
    .invoice-box table tr.top table td {
        padding-bottom: 20px;
    }
    
    .invoice-box table tr.top table td.title {
        font-size: 20px;
        line-height: 45px;
        color: #333;
    }
    
    .invoice-box table tr.information table td {
        padding-bottom: 40px;
    }
    
    .invoice-box table tr.heading td {
        background: #eee;
        border-bottom: 1px solid #ddd;
        font-weight: bold;
    }
    
    .invoice-box table tr.details td {
        padding-bottom: 20px;
    }
    
    .invoice-box table tr.item td{
        border-bottom: 1px solid #eee;
    }
    
    .invoice-box table tr.item.last td {
        border-bottom: none;
    }
    
    .invoice-box table tr.total td:nth-child(2) {
        border-top: 2px solid #eee;
        font-weight: bold;
    }

    
    /** RTL **/
    .rtl {
        direction: rtl;
        font-family: Arial, sans-serif;
    }
    
    .rtl table {
        text-align: right;
    }
    
    .rtl table tr td:nth-child(2) {
        text-align: left;
    }
    </style>
</head>

<body>
    <div class="invoice-box">
        <table cellpadding="0" cellspacing="0">
            <tr class="top">
                <td colspan="2">
                    <table>
                        <tr>
                            <td class="title">
                                <h1>[redacted]</h1>
                            </td>
                            
                            <td>
                                Invoice #: {number}<br>
                                Created: {issueDate}<br>
                                Due: {dueDate}
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
            
            <tr class="information">
                <td colspan="2">
                    <table>
                        <tr>
                            <td>
                                [redacted]<br>
                                [redacted]<br>
                                [redacted]<br>
                                [redacted]<br>
                                [redacted]
                            </td>
                            
                            <td>
                                {company}<br>
                                {name}<br>
                                {email}
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
            <tr class="heading">
                <td>
                    Item
                </td>
                
                <td>
                    Price
                </td>
            </tr>
            
            <!--TABLE-->
            
            <tr class="total">
                <td></td>
                
                <td>
                   Total: £{total}
                </td>
            </tr>
        </table>
    </div>
</body>
</html>

"""

def htmlAddValues(html, number, company, name, email, issueDate, dueDate):
    html = html.replace("{number}",number)
    html = html.replace("{company}",company)
    html = html.replace("{name}",name)
    html = html.replace("{email}",email)
    html = html.replace("{issueDate}",issueDate)
    html = html.replace("{dueDate}",dueDate)
    try:
        int(number)
    except ValueError:
        html.replace("Invoice #:","Invoice Id:")
    return html

def htmlAddTable(html, tableStr, total):
    total = "{:,.2f}".format(total)
    return html.replace(TABLE_MARKER, tableStr).replace("{total}",total)

def tableInput():
    table = []
    while True:
        print("Table size = " + str(len(table)))
        print("Enter an item (e.g. Hosting - 1 year)")
        item = input(" - ")
        print("Enter a price")
        while True:
            try:
                price = float(input(" - £"))
                if price < 0:
                    print("Price cannot be less than 0")
                    continue
            except ValueError:
                print("Enter a valid price")
                continue
            break
        print("Is this ok?")
        print("(y/n)")
        cont = input(" - ")
        if cont.lower() == "y" or cont.lower() == "yes":
            table.append([item,price])
            print("Item added")
        else:
            print("Item not added")
        print()
        print("Continue adding?")
        print("(y/n)")
        cont = input(" - ")
        if not(cont.lower() == "y" or cont.lower() == "yes"):
            break
        else:
            print()
    return table

def formatTable(table):
    tableStr = ""
    total = 0
    for item in table:
        tableStr += TABLE_ENTRY.format(item[0],item[1])
        total += item[1]
    return tableStr, total

def userInput():
    while True:
        number = input("Invoice Number - ")
        company = input("Company Name - ")
        name = input("Invoicee Name - ")
        email = input("Invoicee Email - ")
        print("Is this ok?")
        print("(y/n)")
        cont = input(" - ")
        if cont.lower() == "y" or cont.lower() == "yes":
            break
        else:
            print()
    return number, company, name, email
    

def dateInput():
    while True:
        print("Today is " + formatDate(datetime.date.today()))
        print("How many days from now should the issue date be?")
        while True:
            try:
                issueDays = int(input(" - "))
                if issueDays < 0:
                    print("Must be 0 or more")
                    continue
            except ValueError:
                print("Type a number")
                continue
            break
        print("How many days from the issue date should the due date be?")
        print("30 is the standard")
        while True:
            try:
                dueDays = int(input(" - "))
                if dueDays < 0:
                    print("Must be 0 or more")
                    continue
            except ValueError:
                print("Type a number")
                continue
            break
        now = datetime.date.today()
        issueDate = addDays(now, issueDays)
        dueDate = formatDate(addDays(issueDate, dueDays))
        issueDate = formatDate(issueDate)
        print("This will make the issue date {:s}\nand the due date {:s}.\nIs this ok?".format(issueDate,dueDate))
        print("(y/n)")
        cont = input(" - ")
        if cont.lower() == "y" or cont.lower() == "yes":
            break
        else:
            print()
    return issueDate, dueDate


def addDays(date, toadd):
    return date + datetime.timedelta(days=toadd)

def formatDate(date):
    return date.strftime("%B %d, %Y")

def main():
    number, company, name, email = userInput()
    issueDate, dueDate = dateInput()
    tableStr, total = formatTable(tableInput())
    html = htmlAddValues(BASE_HTML, number, company, name, email, issueDate, dueDate)
    html = htmlAddTable(html, tableStr, total)
    pdfkit.from_string(html, 'out.pdf', options={"quiet":''})
    print(html)

if __name__ == "__main__":
    main()
