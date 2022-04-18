
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10318313
#    Student name: Eugene Martens
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  The Best, Then and Now
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application that allows the user to preview and print lists of
#  top-ten rankings.  See the instruction sheet accompanying this
#  file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.  YOU MAY NOT USE
# ANY NON-STANDARD MODULES SUCH AS 'Beautiful Soup' OR 'Pillow'.  ONLY
# MODULES THAT COME WITH A STANDARD PYTHON 3 INSTALLATION MAY BE
# USED.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen, Request
import datetime
#Dirty Dirty Approuch To fix Security Issues
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from tkinter import *
import os
# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL, sub

# Import the standard SQLite functions (just in case they're
# needed).
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it on a local file and returning its source code
# as a Unicode string. The function tries to produce a
# meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'download',
             filename_extension = 'html'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'});
        web_page = urlopen(req)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#

def access_site(url = 'http://www.wikipedia.org/'):
        # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'});
        web_page = urlopen(req)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Return the downloaded document to the caller
    return web_page_contents

#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

##### DEVELOP YOUR SOLUTION HERE #####

#just cleans up white space mess
def clean_white_spaces(text):
    for i in range(len(text)):
        text[i] = text[i].strip();
    return text;

#grabbing any numerical values from data    
def extract_numbers(text):
    for i in range(len(text)):
        text[i] = findall('[\d.]*\d+', text[i]);
    return text;

#using this as a text scrub to remove anything i dont want in text(&quot)
def phrase_clean_up(text, phrase = " ", replace_to = ""):

    for i in range(len(text)):
        text[i] = text[i].replace(phrase, replace_to);
    return text;

#simple printer helper
def PrintInformation(InformationBlock, limit = 10):
    print("#-----------------------------------------#");
    for i in range(len(InformationBlock)):

        if i <= limit:
            print(InformationBlock[i]);
    print("#-----------------------------------------#");

#merge data into 1 node to access
def create_list_data(data = []):
    newdata = []

    #choosing the length of the first array (hopefully there the same size)
    #will put security measures and clip lists sizes incase of future bugs

    #0 should be titles/name
    #1 should be index
    #2 should be image url
    #3 will be a wildcard, watever is thrown in (rateings, viewings, watever else)
    #4 is the url for the data source
    for i in range(len(data[0])):
            newdata.append([str(data[1][i]), data[0][i], data[3][i], data[2][i], data[4]]);
                       
    return newdata;

#appending a string to current data, like 1000.000 + streams, or 324 "reads"
def add_to_list_item(data, string):
    for i in range(len(data)):
        data[i] = data[i] + string;
    return data;

#more generic fend and replace fuction to help clean up data
def find_and_clean(regex, information):
    for i in range(len(information)):
        information[i] = sub(regex, "", information[i]);
        
    return information;

#Combinging two lists (music titles and artist name in this case), can be expanded incase needed again
def concatenate_lists(listA, listB):
    newlist = []
    for i in range(len(listA)):
        if i > 0:
            if i < len(listB):
                newlist.append(listA[i] + ' -' + listB[i - 1].replace("by",""));
    return newlist;

#download from source, or access archive
#---------------------------------- Book Data Access -------------------------------------------------#
def AcessBookInformation(downloadsource = False):
    
    #Download Book Weekling Top,
    #Grabbing names, now need to cull the list,
    #and grab any relevant information (pictures, dates, links and so on)
    
    #https://www.goodreads.com/book/most_read
    bookreadingdownload = "";
    html_file = "";
    sauce = "";
    #---------------------------------- Download Books ---------------------------------------------#
    if downloadsource:
        print("Accessing......");
        sauce = "https://www.goodreads.com/book/most_read";
        bookreadingdownload = access_site(sauce);
    else:
    #---------------------------------- Archive Music ---------------------------------------------#
        print("Accessing From Archive");
        sauce = "Archived/bookreadingdownload.html";
        html_file = open(sauce, 'r', encoding='utf-8');
        bookreadingdownload = html_file.read();

    #-----Grabbing Book title ---------------------------------------------#
    booktitles = findall("<span itemprop='name'>(.*?)</span>", bookreadingdownload);
    booktitles = find_and_clean(r'\([^()]*\)', booktitles);
    
    #-----Grabbing Book title ---------------------------------------------#
    bookindex = findall('<td valign="top" class="number">(.*?)</td>', bookreadingdownload);
    #-----Grabbing Book img ---------------------------------------------#
    bookimg = findall('itemprop="image" src="(.*?)" />', bookreadingdownload);
    #-----Grabbing Book index ---------------------------------------------#
    bookrating = findall('</span> (.*?) &mdash;', bookreadingdownload, DOTALL);
    #-----Grabbing Book img url ---------------------------------------------#
    bookurl = sauce;
    date = findall('<span class="smallText greyText">(.*?)</span>', bookreadingdownload, DOTALL);
    date = find_and_clean(r'(\t)', date);
    date = find_and_clean(r'(\n)', date);
    date = find_and_clean(r'((generated))', date);
    date = find_and_clean(r'2018 [.*?] ', date);
    date = " ".join(date);
    date = date.split();

    bookdatefinal = date[1] + " " + date[2] + " " + date[3];
    print(bookdatefinal);
    #----Adding Music Data to new Music Node Data List -------------------------------#
    bookfinal = create_list_data([booktitles, bookindex, bookimg, bookrating, bookurl, bookdatefinal]);
    
    #clip list to only 10
    del bookfinal[10:];
    
    #PrintInformation(bookfinal);

    #Close File Read if were not downloading
    if not(downloadsource):
        html_file.close();

    return bookfinal;
#---------------------------------- Book Data Access -------------------------------------------------#

#---------------------------------- Music Data Access -------------------------------------------------#
def AccessMusicInformation(downloadsource = False):
    #https://spotifycharts.com/regional/global/weekly/latest

    musictopdownload = "";
    html_file = "";
    sauce = "";

    #---------------------------------- Download Music ---------------------------------------------#
    if downloadsource:
        print("Accessing......");
        sauce = "https://spotifycharts.com/regional/global/weekly/latest";
        musictopdownload = access_site(sauce);
    else:
    #---------------------------------- Access Music ---------------------------------------------#
        print("Accessing From Archive");
        sauce = "Archived/musictopdownload.html";
        html_file = open(sauce, 'r', encoding='utf-8');
        musictopdownload = html_file.read();


    #---------------------------------- Music Data Cleanup -------------------------------------------------#   
    musictitlesraw = findall('<td class="chart-table-track">(.*?)</td>', musictopdownload, DOTALL);

    #----------------------------------- Fiding and Cleaning Title and Arist ------------------#
    musictitles = findall('<strong>(.*?)</strong>', musictopdownload);
    musictitles = phrase_clean_up(musictitles, "&amp;", "feat.");
    musictitles = phrase_clean_up(musictitles, "&#039;", "'");
    musicartistname = findall('<span>(.*?)</span>', musictopdownload);
    #----------------------------------- Fiding and Cleaning Title------------------#

    #--------Merging Artist and  Title------------------#
    track = concatenate_lists(musictitles, musicartistname);

    #--------Fiding Index -------------------------------#
    musicindex = findall('<td class="chart-table-position">(.*?)</td>', musictopdownload);

    #--------Fiding Image -------------------------------#
    musicimg = findall('<img src="(.*?)">', musictopdownload, DOTALL);

    #--------Fiding Stream Count 
    musicstreams = findall('<td class="chart-table-streams">(.*?)</td>', musictopdownload);
    musicurl = sauce;
    #---------------------------------- Music Data Cleanup -------------------------------------------------#
    
    #musicstreams = add_to_list_item(musicstreams, " streams");
    musicdatefinal = "";
    #----------------------------------- Adding Music Data to new Node Data List -------------------------------#
    musicfinal = create_list_data([track, musicindex, musicimg, musicstreams, musicurl, musicdatefinal]); 
    
    #clip the list
    del musicfinal[10:];
    #PrintInformation(musicfinal);                             
   
    #Close File Read if were not downloading
    if not(downloadsource):
        html_file.close();
        
    return musicfinal;
#---------------------------------- Music Data Access -------------------------------------------------#


#---------------------------------- Electronics Data Access --------------------------------------------#
def AccessElectronicInformation(downloadsource = False):
    #https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics
    electronicstopsaledownload = "";
    html_file = "";
    sauce = "";
    
    if downloadsource :
        print("Accessing......");
        sauce = "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics";
        electronicstopsaledownload = access_site(sauce);
    else:
        print("Accessing From Archive");
        sauce ="Archived/electronicstopsaledownload.html";
        html_file = open(sauce, 'r', encoding='utf-8');
        electronicstopsaledownload = html_file.read();


    electronicstopsaletitle = findall('aria-hidden="true" data-rows=".*?">(.*?)</div>', electronicstopsaledownload, DOTALL);

    #titles were a mess, cleaning up white spaces and anything else in there we dont need
    #will need to fix long ass name issue
    #--------Grabbing Electornic Item Title------------------#
    electronicstopsaletitle = clean_white_spaces(electronicstopsaletitle);
    
    electronicstopsaletitle = phrase_clean_up(electronicstopsaletitle, "&quot", '"');
    electronicstopsaletitle = find_and_clean(r'\([^()]*\)', electronicstopsaletitle);
    electronicstopsaletitle = find_and_clean(r'\|.*$', electronicstopsaletitle);
    #electronicstopsaletitle = find_and_clean(r'\-.*$', electronicstopsaletitle);
    electronicstopsaletitle = find_and_clean(r'\,.*$', electronicstopsaletitle);
    electronicstopsaletitle = find_and_clean(r'\;.*$', electronicstopsaletitle);
    electronicstopsaletitle = find_and_clean(r'\&ndash.*$', electronicstopsaletitle);
    #--------Grabbing Electornic Item Title------------------#

    #--------Grabbing Electornic Item Index ------------------#
    electronicstopsaleindex = findall('<span class="zg-badge-text">(.*?)</span></span><span ', electronicstopsaledownload);
    electronicstopsaleindex = phrase_clean_up(electronicstopsaleindex, "#", "");
    #--------Grabbing Electornic Item Index ------------------#

    #--------Grabbing Electornic Item Image ------------------#
    electronicstopsaleimg = findall('<div class="a-section a-spacing-small"><img alt=".*?" src="(.*?)" height="200" width="200"></div></span>', electronicstopsaledownload);

    #--------Grabbing Electornic Item price ------------------#
    elecontricstopsalerateing = findall(r"<span class='p13n-sc-price'>(.*?:|.*?)</span></span></a>", electronicstopsaledownload);

    #--------Grabbing Electornic Item page source ------------------#
    electronicurl = sauce;
    eleoctronicdate = "";
     #----------------------------------- Adding Music Data to new Node Data List -------------------------------#
    electronicstopsalefinal = create_list_data([electronicstopsaletitle, electronicstopsaleindex, electronicstopsaleimg, elecontricstopsalerateing, electronicurl, eleoctronicdate]);
    
    #clip list to 10 items
    del electronicstopsalefinal[10:];
    #print(electronicstopsalefinal, end ="");
    #PrintInformation(electronicstopsalefinal);

    #Close File Read if were not downloading
    if not(downloadsource):
        html_file.close();

    return electronicstopsalefinal;

#---------------------------------- Electronics Data Access --------------------------------------------#


#Creates a basic Html String, then appends string information
#with added paramateres in html style to export

#Header
#CSS <style>
#date
#banner image
#main Body with information table
#data source
def export_to_html(target_filename, information, title, wildcardtitle, date, banner, banner_suace):
        basic_html = ""
        
        basic_html +="""
        <!DOCTYPE html>
        <html>
        <body>
        
        <style>

        #banner{
        width: 85%;
        display: block;
        margin: 0 auto;
        }
        
        #imgsizeadjust{
            max-width: 150px;
        }
        h2{
            text-align: center;
        }
        table {
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 100%;
        }

        td, th {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }

        #cntr{
        text-align: center;
        }
        </style>
        """
        print(information[5]);
        basic_html += "<h1 id='cntr' >"+title+"</h1>";
        basic_html += "<h2 id=cntr >Week of "+date+"</h2>";
        
        basic_html +="""
        <table>
        <tr>
        <th id='cntr'>Rank</th>
        """

        basic_html += "<img id=banner " + "src=" + banner + ">" + "</td>";
        basic_html += "<p> " + banner_suace + "</p>";

        basic_html +="""
        <th id='cntr'>Image</th>
        <th>Title</th>
        """
        basic_html +="<th>"+wildcardtitle+"</th>"
        basic_html +="</tr>"
        
        for i in range(len(information)):
            basic_html += "<tr>"
            basic_html += "<td id='cntr'>"+ information[i][0] + "</td>"
            basic_html += "<td id='cntr'>" + "<img id=imgsizeadjust " + "src=" + information[i][3] + ">" + "</td>"
            basic_html += "<td>"+ information[i][1] + "</td>"
            basic_html += "<td>"+ information[i][2] + "</td>"
            basic_html += "</tr>";
        basic_html +="""
        </table>
        """
        basic_html +="<p id='cntr'>Data source: "+"<a href=>"+information[0][4]+"</a></p>"
        """
        </body>
        </html>  
        """
        
        #write to file
        text_file = open(target_filename + '.' + "html",
                         'w', encoding = 'UTF-8')
        text_file.write(basic_html);
        text_file.close()
        print("Done");


#preview whichever category was selected by the radio buttons
def preview_information():
    #print(option.get());
    if option.get() == 'B_O':
        print("Accessing Books Old and Previewing");
        display_information(AcessBookInformation(False), preview_B_img, "Previous Most Read Books");
    elif option.get() == 'B_N':
        print("Accessing Books New and Previewing");
        display_information(AcessBookInformation(True), preview_B_img, "Current Most Read Books");
    elif option.get() == 'M_O':
        print("Accessing Music Old and Previewing");
        display_information(AccessMusicInformation(False), preview_M_img, "Previous Most Streamed Music");
    elif option.get() == 'M_N':
        print("Accessing Music New and Previewing");
        display_information(AccessMusicInformation(True), preview_M_img, "Current Most Streamed Music");
    elif option.get() == 'E_O':
        print("Accessing Electronics Old and Previewing");
        display_information(AccessElectronicInformation(False), preview_E_img, "Previous Most Bought Electronics");
    elif option.get() == 'E_N':
        print("Accessing Electronics New and Previewing");
        display_information(AccessElectronicInformation(True), preview_E_img, "Current Most Bought Electronics");


#export newly created HTML document to /exports folder Fork Function
#based on radiobutton option mode
def export_information():
    #print(option.get());

    #http://fortbragglibrary.org/winter-reading/book-banner-5/
    #https://pt.pngtree.com/freebackground/musical-symbol-background_379008.html
    
    now = datetime.datetime.now();
    datestring = now.strftime("%B") + " " + str(now.day) + " " + str(now.year);
    if option.get() == 'B_O':
        print("Accessing Books Old and Exporting");
        datestring = "September 29 2018";
        export_to_html("Export/Books_Read_Previous", AcessBookInformation(False), "Previous Most Read Books", "Ratings", datestring, "http://fortbragglibrary.org/wp-content/uploads/2017/12/Book-banner.jpg", ""); 
    elif option.get() == 'B_N':
        print("Accessing Books New and Exporting");
        export_to_html("Export/Books_Read_Current", AcessBookInformation(True), "Current Most Read Books", "Ratings", datestring, "http://fortbragglibrary.org/wp-content/uploads/2017/12/Book-banner.jpg", ""); 
    elif option.get() == 'M_O':
        print("Accessing Music Old and Exporting");
        datestring = "October 4 2018";
        export_to_html("Export/Music_Streamed_Previous", AccessMusicInformation(False), "Previous Most Streamed Music", "Streamed", datestring, "https://png.pngtree.com/thumb_back/fw800/back_pic/02/97/25/715790ced7e3a3b.jpg", "");
    elif option.get() == 'M_N':
        print("Accessing Music New and Exporting");
        export_to_html("Export/Music_Streamed_Current", AccessMusicInformation(True), "Current Most Streamed Music", "Streamed", datestring, "https://png.pngtree.com/thumb_back/fw800/back_pic/02/97/25/715790ced7e3a3b.jpg", "");
    elif option.get() == 'E_O':
        print("Accessing Electronics Old and Exporting");
        datestring = "September 30 2018";
        export_to_html("Export/Electronics_Bought_Previous", AccessElectronicInformation(False), "Previous Most Bought Electronics", "Price", datestring, "http://www.uggroups.com/wp-content/uploads/2018/01/Electronics-1.jpg", "");
    elif option.get() == 'E_N':
        print("Accessing Electronics New and Exporting");
        export_to_html("Export/Electronics_Bought_Current", AccessElectronicInformation(True), "Current Most Bought Electronics", "Price", datestring, "http://www.uggroups.com/wp-content/uploads/2018/01/Electronics-1.jpg", "");


#save information to database Fork Function
#based on radiobutton option mode
def save_information():
    #print(option.get());
    now = datetime.datetime.now();
    datestring = now.strftime("%B") + " " + str(now.day) + " " + str(now.year);
    if option.get() == 'B_O':
        print("Accessing Books Old and Saving");
        datestring = "September 29 2018";
        save_to_database(AcessBookInformation(False), datestring);
    elif option.get() == 'B_N':
        print("Accessing Books New and Saving");
        save_to_database(AcessBookInformation(True), datestring);
    elif option.get() == 'M_O':
        print("Accessing Music Old and Saving");
        datestring = "October 4 2018";
        save_to_database(AccessMusicInformation(False), datestring);
    elif option.get() == 'M_N':
        print("Accessing Music New and Saving");
        save_to_database(AccessMusicInformation(True), datestring);
    elif option.get() == 'E_O':
        print("Accessing Electronics Old and Saving");
        datestring = "September 30 2018";
        save_to_database(AccessElectronicInformation(False), datestring);
    elif option.get() == 'E_N':
        print("Accessing Electronics New and Saving");
        save_to_database(AccessElectronicInformation(True), datestring);

#function name says it all :P
def save_to_database(information, date):
    print('Data Being Saved....');
    connection = connect('top_ten.db');

    with connection:
        cur = connection.cursor();
        for i in range(len(information)):
            cur.execute("INSERT INTO top_ten VALUES(?,?,?,?)", (date,information[i][0], information[i][1], information[i][3]));
    print('Data Saved Succesfully');


#creates new window and display the informations            
def display_information(information, windowimage, title):
    new_window = Toplevel(window);
    new_window.geometry("800x300");
    new_window.configure(background='white');
    
    #-----------------------------Image--------------------------------------------#
    #image holder
    leftFrame = Frame(new_window, width = 200, height = 600);
    leftFrame.grid(row=0,column=0, padx=0,pady=0, sticky=NSEW);
    leftFrame.configure(background='white');

    
    ImageLabel = Label(leftFrame, image = windowimage);
    ImageLabel.grid(row = 0, column = 0);
    ImageLabel.configure(background='white');
    #-----------------------------Image--------------------------------------------#


    #-----------------------------Data List Display--------------------------------------------#    
    rightFrame = Frame(new_window, width = 100, height = 5, borderwidth = 5);
    rightFrame.grid(row=0,column=1, padx=0,pady=25, sticky=NSEW);
    rightFrame.configure(background='white');

    MostReadFrame = Frame(rightFrame, width = 100);
    MostReadFrame.grid(row=0,column=0, padx=0,pady=0, sticky=NSEW);
    MostReadFrame.configure(background='white');

    #-------------Data --------------------------------------------#
    indexLabel = Text(MostReadFrame, width = 3, relief="flat", fg='#E59258', font='Helvetica 10 bold');
    indexLabel.grid(row = 2, column = 0, padx=0,pady=(15, 19), sticky=W);
    indexLabel.configure(background='white');

    displayLabel = Text(MostReadFrame, width = 45,  relief="flat", fg='#5896E5', font='Helvetica 10 bold');
    displayLabel.grid(row = 2, column = 1, padx=0,pady=(15, 19), sticky=W);
    displayLabel.configure(background='white');
    #------------Data --------------------------------------------#

    #-------------Title --------------------------------------------#
    titleLabel = Label(MostReadFrame, text=title, width = 30, height = 1, font='Helvetica 18 bold');
    titleLabel.grid(row=0,column=1, padx=0,pady=0, sticky=NSEW);
    titleLabel.configure(background='white');
    #-------------Title --------------------------------------------#

    #----------Adding List Infomration to there Text Boxes--------------------------#
    maxstringlength = 40;
    for i in range(len(information)):
        if len(information[i][1]) > maxstringlength:
            information[i][1] = information[i][1][:maxstringlength];
            information[i][1]+=("...");

        displayLabel.insert(END,(information[i][1] + "\n"))
        indexLabel.insert(END, "[" + str(i) + "]" + "\n");
    #---------Adding List Infomration to there Text Boxes--------------------------#
        
    new_window.grid_rowconfigure(0, weight=1)
    new_window.grid_rowconfigure(1, weight=1)
    new_window.grid_rowconfigure(2, weight=1)
    new_window.grid_rowconfigure(3, weight=1)
    new_window.grid_columnconfigure(0, weight=1)
    new_window.grid_columnconfigure(2, weight=1)
 #-----------------------------Data List--------------------------------------------#


#----------------------------------------- Main Window Setup-----------------------------#   
window = Tk();
window.title("Spicy Data");
window.geometry("600x300");
window.configure(background='white');

textfont = ('Ariel bold', 12);
#----------------------------------------- Main Window Setup-----------------------------#


#----------------------------------------- Main Image Setup-----------------------------#

leftFrame = Frame(window, width = 200, height = 600);
leftFrame.grid(row=0,column=0, padx=0,pady=0, sticky=NSEW);
leftFrame.configure(background='white');

img = PhotoImage(file = "images/main.gif");
ChillImageLabel = Label(leftFrame, image = img);
ChillImageLabel.grid(row = 0, column = 0);
ChillImageLabel.configure(background='white');
#----------------------------------------- Main Image Setup-----------------------------#


#----------------------------------------- Radio Buttons Setup-----------------------------#

#Mode codes for radio button values
#O = Old/Prevois, N = New
#B = Book, M = Music, E = Electronics
MODES = [
    ("B_O"),
    ("B_N"),
    ("M_O"),
    ("M_N"),
    ("E_O"),
    ("E_N"),
    ]


rightFrame = Frame(window, width = 100, height = 5, borderwidth = 5);
rightFrame.grid(row=0,column=1, padx=0,pady=20, sticky=NSEW);
rightFrame.configure(background='white');

option = StringVar()
option.set("B_O") # initialize radio button selection


#------------------------------ Books Radio Buttons ------------------------------#   
MostReadFrame = LabelFrame(rightFrame, text="Most Read Books", width = 25, height = 3, borderwidth = 2, relief = GROOVE);
MostReadFrame.grid(row=0,column=0, padx=5,pady=5, sticky=NSEW);
MostReadFrame.configure(background='white');

#Extra Space Creater
dud = Label(MostReadFrame, width = 3);
dud.grid(row = 0, column = 0, padx=(0), pady=(0));
dud.configure(background='white');

#Prev Radio Button
MostListenedPreviousRadial = Radiobutton(MostReadFrame, text="Previous", width = 10,indicatoron=0, var=option, value=MODES[0], selectcolor ='#AEE1FF', borderwidth = 1,  font = textfont);
MostListenedPreviousRadial.grid(row = 0, column = 1, padx=(5), pady=(5));
MostListenedPreviousRadial.configure(background='white');

#Current Radio Button
MostListenedCurrentRadial= Radiobutton(MostReadFrame, text="Current", width = 10, indicatoron=0, var=option, value=MODES[1], selectcolor ='#AEE1FF', borderwidth = 1,  font = textfont);
MostListenedCurrentRadial.grid(row = 0, column = 3, padx=(5), pady=(5));
MostListenedCurrentRadial.configure(background='white');
#------------------------------ Books Radio Buttons ------------------------------#


#------------------------------ Music Radio Buttons ------------------------------#
MostListenframe = LabelFrame(rightFrame, text="Most Listened To Music", width = 25, height =3, borderwidth = 2, relief = GROOVE);
MostListenframe.grid(row=1,column=0,  padx=5,pady=5, sticky=NSEW);
MostListenframe.configure(background='white');

dud = Label(MostListenframe, width = 3);
dud.grid(row = 0, column = 0, padx=(0), pady=(0));
dud.configure(background='white');

MostListenedPreviousRadial = Radiobutton(MostListenframe, text="Previous", width = 10, indicatoron=0, var=option, value=MODES[2], selectcolor ='#AEE1FF', borderwidth = 1,  font = textfont);
MostListenedPreviousRadial.grid(row = 0, column = 1, padx=(5), pady=(5));
MostListenedPreviousRadial.configure(background='white');

MostListenedCurrentRadial= Radiobutton(MostListenframe, text="Current", width = 10, indicatoron=0, var=option, value=MODES[3], selectcolor ='#AEE1FF', borderwidth = 1,  font = textfont);
MostListenedCurrentRadial.grid(row = 0, column = 2, padx=(5), pady=(5));
MostListenedCurrentRadial.configure(background='white');
#------------------------------ Music Radio Buttons ------------------------------#


#------------------------------ Electronics Radio Buttons ------------------------------#
MostBoughtFrame = LabelFrame(rightFrame, text="Most Bought Electronics", width = 25, height =3, borderwidth = 2, relief = GROOVE);
MostBoughtFrame.grid(row=2,column=0, padx=5,pady=5, sticky=NSEW);
MostBoughtFrame.configure(background='white');

dud = Label(MostBoughtFrame, width = 3);
dud.grid(row = 0, column = 0, padx=(0), pady=(0));
dud.configure(background='white');

MostListenedPreviousRadial = Radiobutton(MostBoughtFrame, text="Previous", width = 10, indicatoron=0, var=option, value=MODES[4], selectcolor ='#AEE1FF', borderwidth = 1,  font = textfont);
MostListenedPreviousRadial.grid(row = 0, column = 1, padx=(5), pady=(5));
MostListenedPreviousRadial.configure(background='white');

MostListenedCurrentRadial= Radiobutton(MostBoughtFrame, text="Current", width = 10, indicatoron=0, var=option, value=MODES[5], selectcolor ='#AEE1FF', borderwidth = 1,  font = textfont);
MostListenedCurrentRadial.grid(row = 0, column = 2, padx=(5), pady=(5));
MostListenedCurrentRadial.configure(background='white');
#------------------------------ Electronics Radio Buttons ------------------------------#

#------------------------------ Image Download And Save ------------------------------#
preview_B_img = PhotoImage(file = "images/book.gif");
preview_M_img = PhotoImage(file = "images/music.gif");
preview_E_img = PhotoImage(file = "images/electronics.gif");
#------------------------------ Image Download And Save ------------------------------#

#------------------------------ Output Buttons ------------------------------#
OutputButtonFrame = Frame(rightFrame, width = 20, height = 10, borderwidth = 1);
OutputButtonFrame.grid(row=3,column=0, padx=0,pady=10, sticky=N);
OutputButtonFrame.configure(background='white');

CurrentButton = Button(OutputButtonFrame, text="Export", width = 10, command = export_information);
CurrentButton.grid(row = 0, column = 1, padx=(5), pady=(5));

PrevButton = Button(OutputButtonFrame, text="Preview", width = 10, command = preview_information);
PrevButton.grid(row = 0, column = 2, padx=(5), pady=(5));

SaveButton = Button(OutputButtonFrame, text="Save", width = 10, command = save_information);
SaveButton.grid(row = 0, column = 0, padx=(10), pady=(5));
#------------------------------ Output Buttons ------------------------------#

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(2, weight=1)


window.mainloop();


print(option);





