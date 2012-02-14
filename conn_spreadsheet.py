#!/usr/bin/env python

import sys
import getopt
import getpass

#import gdata.spreadsheet.text_db
from gdata.spreadsheet.service import SpreadsheetsService

class SpreadSheet :
  def __init__(self, user, pw) :
    self.document_name = ''
    self.current_key = ''

    # Login process
    self.gd_client = SpreadsheetsService()
    self.gd_client.email = user
    self.gd_client.password = pw
    self.gd_client.ProgrammaticLogin()

  def set_document(self, name) :
     self.document_name = name
     self._get_current_key()
    
  def _get_current_key(self) :
     feed = self.gd_client.GetSpreadsheetsFeed()
     for entry in feed.entry :
       if entry.title.text == self.document_name :
         self.current_key = entry.id.text.split('/')[-1]
         break
       else :
         raise ValueError('document no found')

  def _get_worksheet_index(self) :
     wksht_idx = len(self.gd_client.GetWorksheetsFeed(key=self.current_key).entry) - 1
     #print "Worksheet Index:", wksht_idx
     return wksht_idx

  def get_current_key(self) :
    return self.current_key

  def get_worksheet_id(self) :
     wksht_idx = self._get_worksheet_index()
     wksht_id = self.gd_client.GetWorksheetsFeed(key=self.current_key).entry[wksht_idx].id.text.rsplit('/', 1)[1]
 
     #print "Worksheet ID:", wksht_id
     return wksht_id

  def create_worksheet(self, name) :
     worksheet = self.gd_client.AddWorksheet(title=name, row_count=100, col_count=20, key=self.current_key)

  def insert_row(self, data, wksht_id) :
     for i, row in enumerate(data) :
       for j, value in enumerate(row) :
         self.gd_client.UpdateCell(row=i + 1, col=(j + 1), inputValue=value, key=self.current_key, wksht_id=wksht_id)

if __name__ == '__main__' :
  user = sys.argv[1:]
  print user[0]
  pw = getpass.getpass('Password for %s:' % user[0])

  conn = Spreadsheet(user[0], pw)
