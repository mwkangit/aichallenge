from http import HTTPStatus
import pymysql
from flask import Flask, jsonify, redirect, render_template, request, url_for
from selectQuery import InsertQuery

insQuery=InsertQuery(1113444)

print(insQuery.selectHistory())