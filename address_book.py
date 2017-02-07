import sys
import _pickle as pickle
import pdb

file = 'address_book.data'
addlist = []

def dump():
  '''save to data file

  when press enter, this function will be fired'''

  try:
    f = open(file, 'rb')
    listmp = pickle.load(f)
  except:
    listmp = []

  with open(file, 'wb') as f:
    # pdb.set_trace()
    pickle.dump(addlist+listmp, f, True)

  with open(file, 'rb') as f:
    print(pickle.load(f))


while True:
  try:
    args = input('Please enter the name and phone (ctrl+d to cancel):\n')
    name, phone = args.split(' ')
    addlist.append({'name': name, 'phone': phone})

  except ValueError:
    if args == '':
      dump()
      break
    else:
      print('ERROR: wrong name or phone')

  except EOFError:
    print('')
    break
