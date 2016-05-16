import os
import configparser
from flask_script import Manager, Command
from vendcli import (
        app,
        views,
        )
from vendcli.models.meta import (
        engine,
        Session
        )
from vendcli.models import Transaction, Source

manager = Manager(app)
session = Session()

source_list = session.query(Source)

@manager.command
def cash_pull():
    denom = {1:'Single',5:'Five',10:'Ten',20:'Twenty',50:'Fifty',100:'Hundred'}
    value = [1,5,10,20,50,100]
    for i in range(0,6):
        amount = cli.prompt('Please enter the total for '+denom[value[i]]+'s')


@manager.command
def coin_pull():
    denom = {100:'Dollar',50:'Fifty-cent',25:'Quarter',10:'Dime',5:'Nickle',1:'Penny'}
    value = [100,50,25,10,5,1]
    for d in value:
        amount = cli.prompt('Please enter the total for '+denom[d]+'s')

@manager.command
def add_expense():
    new_purv = cli.prompt_choice('Is this for an existing purveyor?',default='y')
    if(new_purv):
        ptypecli.prompt_choices('Purveyor type:')
        acct=cli.prompt('Account Number')
        pnum=cli.prompt('Phone Number')
        addr=cli.prompt('Street Address')
        addr2=cli.prompt('Street Address 2')
        city=cli.prompt('City')
        state=cli.prompt('State Code')
        postal=cli.prompt('Postal Code')
#        purv_num=generate_purveyor(pname=name,pacct=acct,pnum=pnum,saddr=addr,saddr2=addr2,city=city,postal=postal)
    else:
        purv_num = cli.prompt('Purveyor Number')
    exp_date=cli.prompt('Date of Expense')
    amount=cli.prompt('Total Expense')
    supply=cli.prompt('Cost of Supplies')
    other=cli.prompt('Other Expenses')

if(__name__=='__main__'):
    manager.run()

