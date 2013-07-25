
import os, sys
import getopt
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3 #@UnresolvedImport
from mutagen.id3 import ID3, TOPE, TDRC, TPE2, TPE1, TALB, TRCK, TIT2, TCON, TENC, COMM, TCOM #@UnresolvedImport

_version = 0.01
_directory = ""
_analyze = 0
_expression = ""
_print = 0

class mp3FileInfo:

    def __init__(self, filename=None, filter=None):
        self.filepath = filename
        self.filename = os.path.basename(filename)
        self.foldername = os.path.split(os.path.split(filename)[0])[1]
        self.id3tags = MP3(filename)
        self.cleanfile = self.filename
        self.fileisclean = False
        self.id3isclean = False
        #self.cleanTags(filter)

    def cleanFilename(self, filter):
        temp = self.filename.replace(filter, '')
        temp = temp.strip()
        self.cleanfile = temp
        self.fileisclean = True

    def cleanTags(self, filter):
        self.cleanid3Tags = {}
        keys = self.id3tags.keys()
        for key in keys:
            if filter in key:
                newkey = key.replace(filter, '')
            else:
                newkey = key
            if key != 'APIC:':
                temp = str(self.id3tags[key])
                if filter in temp:
                    temp = temp.replace(filter, '')
                    temp = temp.strip()
                    if temp.endswith('-'):
                        temp = temp.rstrip('-')
                        temp = temp.rstrip()
                    if temp.startswith('-'):
                        temp = temp.lstrip('-')
                        temp = temp.lstrip()
                self.cleanid3Tags[newkey] = temp
            else:
                self.cleanid3Tags[newkey] = self.id3tags[key]
        self.id3isclean = True

    def getAllID3Tgs(self):
        return self.id3tags

    def printTags(self, type=0):
        if type == 0:
            keys = self.id3tags.keys()
            for key in keys:
                if key != 'APIC:':
                    print "%s -> %s" % (key, self.id3tags[key])
                else:
                    print "APIC: exists"
        else:
            keys = self.cleanid3Tags.keys()
            for key in keys:
                if key != 'APIC:':
                    if self.cleanid3Tags[key]:
                        print "%s -> %s" % (key, self.cleanid3Tags[key])
                else:
                    print "APIC: exists"

def version():
    print "mp3cleaner: Version " + str(_version)

def usage():
    print __doc__

def savecleantags(params):

    fileList = params['mp3files']
    _expression = params['expr']
    _compare = params['compare']
    _print = params['print']

    myList = []
    for file in fileList:
        myfile = mp3FileInfo(file, _expression)
        myfile.cleanTags(_expression)
        myList.append(myfile)


    if _compare:
        print "###########Begin Analyzing"
        for item in myList:
            print "File Path: " + item.filepath
            print "File Name: " + item.filename
            print "Folder Name: "  + item.foldername
            print "-------start old tags---------"
            item.printTags()
            print "--------end old tags--------"
            print "--------start new tags--------"
            item.printTags(1)
            print "--------end new tags--------"
        print "###########End Analyzing"
        exit()

    #if print, just print and exit
    if _print:
        print "\n###########Current Tags"
        for item in myList:
            print "File: " + item.filepath
            item.printTags()
        exit()

    print "Start Cleaning tags on %d files" % len(myList)

    #start cleanup
    for item in myList:
        filename = item.filepath

        newtags = ID3()
        #newtags = ID3(filename)
        tagkeys = item.cleanid3Tags


        for tagkey in tagkeys:
            if tagkey == 'TOPE':
                if isinstance(tagkeys[tagkey], unicode):
                    newtags['TOPE'] = TOPE(encoding=3, text=tagkeys[tagkey])
                else:
                    newtags['TOPE'] = TOPE(encoding=3, text=unicode(tagkeys[tagkey], errors='ignore'))
            elif tagkey == 'TDRC':
                if isinstance(tagkeys[tagkey], unicode):
                    newtags['TDRC'] = TDRC(encoding=3, text=tagkeys[tagkey])
                else:
                    newtags['TDRC'] = TDRC(encoding=3, text=unicode(tagkeys[tagkey], errors='ignore'))
            elif tagkey == 'TPE2':
                if isinstance(tagkeys[tagkey], unicode):
                    newtags['TPE2'] = TPE2(encoding=3, text=tagkeys[tagkey])
                else:
                    newtags['TPE2'] = TPE2(encoding=3, text=unicode(tagkeys[tagkey], errors='ignore'))
            elif tagkey == 'TPE1':
                if isinstance(tagkeys[tagkey], unicode):
                    newtags['TPE1'] = TPE1(encoding=3, text=tagkeys[tagkey])
                else:
                    newtags['TPE1'] = TPE1(encoding=3, text=unicode(tagkeys[tagkey], errors='ignore'))
            elif tagkey == 'TALB':
                if isinstance(tagkeys[tagkey], unicode):
                    newtags['TALB'] = TALB(encoding=3, text=tagkeys[tagkey])
                else:
                    newtags['TALB'] = TALB(encoding=3, text=unicode(tagkeys[tagkey], errors='ignore'))
            elif tagkey == 'TRCK':
                if isinstance(tagkeys[tagkey], unicode):
                    newtags['TRCK'] = TRCK(encoding=3, text=tagkeys[tagkey])
                else:
                    newtags['TRCK'] = TRCK(encoding=3, text=unicode(tagkeys[tagkey], errors='ignore'))
            elif tagkey == 'TIT2':
                if isinstance(tagkeys[tagkey], unicode):
                    newtags['TIT2'] = TIT2(encoding=3, text=tagkeys[tagkey])
                else:
                    newtags['TIT2'] = TIT2(encoding=3, text=unicode(tagkeys[tagkey], errors='ignore'))
            elif tagkey == 'TCON':
                if isinstance(tagkeys[tagkey], unicode):
                    newtags['TCON'] = TCON(encoding=3, text=tagkeys[tagkey])
                else:
                    newtags['TCON'] = TCON(encoding=3, text=unicode(tagkeys[tagkey], errors='ignore'))
            elif tagkey == 'TENC':
                if isinstance(tagkeys[tagkey], unicode):
                    newtags['TENC'] = TENC(encoding=3, text=tagkeys[tagkey])
                else:
                    newtags['TENC'] = TENC(encoding=3, text=unicode(tagkeys[tagkey], errors='ignore'))
            elif tagkey == 'COMM':
                if isinstance(tagkeys[tagkey], unicode):
                    newtags['COMM'] = COMM(encoding=3, text=tagkeys[tagkey])
                else:
                    newtags['COMM'] = COMM(encoding=3, text=unicode(tagkeys[tagkey], errors='ignore'))
            elif tagkey == 'TCOM':
                if isinstance(tagkeys[tagkey], unicode):
                    newtags['TCOM'] = TCOM(encoding=3, text=tagkeys[tagkey])
                else:
                    newtags['TCOM'] = TCOM(encoding=3, text=unicode(tagkeys[tagkey], errors='ignore'))
            elif tagkey == 'APIC:':
                newtags['APIC'] = tagkeys[tagkey]


        #delete old tags
        tagfiledel = MP3(filename)
        tagfiledel.delete()
        #tagfiledel.delete(filename)
        #tagfiledel.save()
        # save new tags
        newtags.save(filename)
        print 'Fixed tags on ' + filename
    print "Finished cleaning tags"

    return

def rename(params):
    #print "Start renaming files"
    fileList = params['mp3files']
    _expression = params['expr']
    _compare = params['compare']
    _print = params['print']

    if _print:
        print "Begin Printing Original file name[s]"
        for file in fileList:
            filename = os.path.basename(file)
            print filename
        print "End Printing"
        exit()

    if _compare:
        print "Begin investigating filename changes"
    else:
        print "Begin Renaming files"

    processedCount = 0
    for file in fileList:
        filename = os.path.basename(file)
        foldername = os.path.dirname(file)

        newname = ""
        if _expression in filename:
            newname = filename.replace(_expression,'')
            newname = newname.strip()
            if not _compare:
                os.rename(file, os.path.join(foldername,newname))
            processedCount = processedCount + 1
            print "Rename " + filename + " ==> "
            if not _compare:
                print "To     " + newname + " complete."
            else:
                print "To     " + newname

    if _compare:
        print "End investigation"
    else:
        print "End Renaming files"

    if not _compare:
        print "\nSummary"
        print "Total Files processed: " + str(len(fileList))
        if processedCount > 0:
            print "Total Files renamed: " + str(processedCount)

    return

def investigate(params):
    fileList = params['mp3files']

    for file in fileList:
        filename = os.path.basename(file)
        print "Filename: ", filename
        audio = MP3(filename, ID3=EasyID3)
        for key in sorted(audio.keys()):
            print "%15s : %s" % (key, audio[key])




def main(argv):
    global _directory
    global _displaydetails

    #print 'ARGV      :', sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "hva:t:e:ipc", ["help", "version", "action=", "target=", "expression=", "investigate", "print", "compare"])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    #print 'OPTIONS   :', opts

    if not opts:
        version()
        usage()
        exit()

    _target = ""
    _investigate = 0
    _compare = 0
    _expression = ""
    _print = 0
    _action = ""
    _rename = None
    _cleantag = None
    _isdir = None

    for o, a in opts:
        if o in ("-h", "--help"):
            version()
            usage()
            exit()
        elif o in ("-v", "--version"):
            version()
            exit()
        elif o in ("-t","--target"):
            _target = a
        elif o in ("-e", "--expression"):
            _expression = a
        elif o in ("-a", "--action"):
            _action = a
        elif o in ("-i", "--investigate"):
            _investigate = 1
        elif o in ("-c", "--compare"):
            _compare = 1
        elif o in ("-p", "--print"):
            _print = 1
        else:
            assert False, "unhandled option"

    if not _target:
        _target = os.getcwd()
        _isdir = True
    else:
        if os.path.isdir(_target):
            _isdir = True
        elif os.path.isfile(_target):
            _isdir = False
        else:
            print "Target  %s is neither a file not a directory!" % _target
            print "Retry with a valid target"
            usage()
            exit()

    if not _investigate:
        if not _action:
            print "No Action provided!!"
            usage()
            exit()

    if _action == "rename":
        _rename = True
    else:
        _rename = False
    if _action == "cleantag":
        _cleantag = True
    else:
        _cleantag = False

    if _action:
        if not (_rename or _cleantag):
            print "Actions can only be rename or cleantag"
            usage()
            exit()

    print "Processing: " + _target
    if not _investigate:
        print "Action: " + _action
    if _expression:
        print "Cleaning filter: " + _expression

    fileList = []
    if _isdir:
        for root, dirs, files in os.walk(_target):
            for name in files:
                filename = os.path.join(root,name)
                if filename.lower().endswith('.mp3'):
                    fileList.append(filename)
    else:
        if _target.lower().endswith('.mp3'):
            fileList.append(_target)

    if not _investigate:
        if not _expression:
            print "No Filter provided to clean!!"
            usage()
            exit()
    else:
        print "Start investigating target"
        parms = {}
        parms['mp3files'] = fileList
        investigate(parms)
        exit()

    params = {}
    params['mp3files'] = fileList
    params['expr'] = _expression
    params['compare'] = _compare
    params['print'] = _print

    if _rename:
        rename(params)
    else:
        savecleantags(params)


if __name__ == '__main__':
    main(sys.argv[1:])

