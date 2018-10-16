/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.entity;

import java.io.Serializable;
import java.util.Collection;
import javax.persistence.Basic;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.Lob;
import javax.persistence.ManyToMany;
import javax.persistence.ManyToOne;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlTransient;

/**
 *
 * @author agno3
 */
@Entity
@Table(name = "user")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "User.findAll", query = "SELECT u FROM User u")
    , @NamedQuery(name = "User.findByUserId", query = "SELECT u FROM User u WHERE u.userId = :userId")
    , @NamedQuery(name = "User.findByUserPasswd", query = "SELECT u FROM User u WHERE u.userPasswd = :userPasswd")
    , @NamedQuery(name = "User.findByUserEmail", query = "SELECT u FROM User u WHERE u.userEmail = :userEmail")
    , @NamedQuery(name = "User.findByUserPhone", query = "SELECT u FROM User u WHERE u.userPhone = :userPhone")
    , @NamedQuery(name = "User.findByUserAvatar", query = "SELECT u FROM User u WHERE u.userAvatar = :userAvatar")
    , @NamedQuery(name = "User.findByUserIdenity", query = "SELECT u FROM User u WHERE u.userIdenity = :userIdenity")
    , @NamedQuery(name = "User.findByUserName", query = "SELECT u FROM User u WHERE u.userName = :userName")
    , @NamedQuery(name = "User.findByUserWechat", query = "SELECT u FROM User u WHERE u.userWechat = :userWechat")
    , @NamedQuery(name = "User.findByUserAlipay", query = "SELECT u FROM User u WHERE u.userAlipay = :userAlipay")})
public class User implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Basic(optional = false)
    @Column(name = "user_id")
    private Integer userId;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 20)
    @Column(name = "user_passwd")
    private String userPasswd;
    @Size(max = 45)
    @Column(name = "user_email")
    private String userEmail;
    @Size(max = 15)
    @Column(name = "user_phone")
    private String userPhone;
    @Size(max = 45)
    @Column(name = "user_avatar")
    private String userAvatar;
    @Basic(optional = false)
    @NotNull
    @Column(name = "user_idenity")
    private int userIdenity;
    @Size(max = 45)
    @Column(name = "user_name")
    private String userName;
    @Size(max = 15)
    @Column(name = "user_wechat")
    private String userWechat;
    @Size(max = 15)
    @Column(name = "user_alipay")
    private String userAlipay;
    @Lob
    @Size(max = 65535)
    @Column(name = "user_info")
    private String userInfo;
    @ManyToMany(mappedBy = "userCollection")
    private Collection<Administrator> administratorCollection;
    @JoinColumn(name = "mainpage_main_id", referencedColumnName = "main_id")
    @ManyToOne(optional = false)
    private Mainpage mainpageMainId;

    public User() {
    }

    public User(Integer userId) {
        this.userId = userId;
    }

    public User(Integer userId, String userPasswd, int userIdenity) {
        this.userId = userId;
        this.userPasswd = userPasswd;
        this.userIdenity = userIdenity;
    }

    public Integer getUserId() {
        return userId;
    }

    public void setUserId(Integer userId) {
        this.userId = userId;
    }

    public String getUserPasswd() {
        return userPasswd;
    }

    public void setUserPasswd(String userPasswd) {
        this.userPasswd = userPasswd;
    }

    public String getUserEmail() {
        return userEmail;
    }

    public void setUserEmail(String userEmail) {
        this.userEmail = userEmail;
    }

    public String getUserPhone() {
        return userPhone;
    }

    public void setUserPhone(String userPhone) {
        this.userPhone = userPhone;
    }

    public String getUserAvatar() {
        return userAvatar;
    }

    public void setUserAvatar(String userAvatar) {
        this.userAvatar = userAvatar;
    }

    public int getUserIdenity() {
        return userIdenity;
    }

    public void setUserIdenity(int userIdenity) {
        this.userIdenity = userIdenity;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getUserWechat() {
        return userWechat;
    }

    public void setUserWechat(String userWechat) {
        this.userWechat = userWechat;
    }

    public String getUserAlipay() {
        return userAlipay;
    }

    public void setUserAlipay(String userAlipay) {
        this.userAlipay = userAlipay;
    }

    public String getUserInfo() {
        return userInfo;
    }

    public void setUserInfo(String userInfo) {
        this.userInfo = userInfo;
    }

    @XmlTransient
    public Collection<Administrator> getAdministratorCollection() {
        return administratorCollection;
    }

    public void setAdministratorCollection(Collection<Administrator> administratorCollection) {
        this.administratorCollection = administratorCollection;
    }

    public Mainpage getMainpageMainId() {
        return mainpageMainId;
    }

    public void setMainpageMainId(Mainpage mainpageMainId) {
        this.mainpageMainId = mainpageMainId;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (userId != null ? userId.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof User)) {
            return false;
        }
        User other = (User) object;
        if ((this.userId == null && other.userId != null) || (this.userId != null && !this.userId.equals(other.userId))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "com.entity.User[ userId=" + userId + " ]";
    }
    
}
